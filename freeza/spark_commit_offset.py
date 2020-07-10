from kafka import KafkaConsumer
from kafka import TopicPartition
from kafka import OffsetAndMetadata

import time
import threading


def __commit_offsets(query, consumer):
    if query.lastProgress == None:
        return
    for offsets in query.lastProgress['sources']:
        end_offsets = offsets['endOffset']
        if end_offsets == None:
            continue
        for topic in end_offsets.keys():
            for partition in end_offsets[topic].keys():
                offset = end_offsets[topic][partition]
                topic_partition = TopicPartition(topic, int(partition))
                consumer.assign([topic_partition])
                consumer.commit(
                    {topic_partition: OffsetAndMetadata(offset, None)})


def start_commiter(query, bootstrap_servers, group_id, sleep_time=5, **kwargs):
    options = {
        "auto_offset_reset": "earliest",
        "bootstrap_servers": bootstrap_servers,
        "group_id": group_id,
        "api_version": "2.4.0",
        **kwargs
    }

    consumer = KafkaConsumer(**options)

    if query == None or not query.isActive:
        check_count = 0
        while check_count < 5 and (query == None or not query.isActive):
            time.sleep(5)
            check_count += 1

    while True:
        __commit_offsets(query, consumer)
        if not query.isActive:
            break
        time.sleep(sleep_time)

def start_commiter_thread(query,  bootstrap_servers, group_id, sleep_time=5, **kwargs):
    thread = threading.Thread(target=start_commiter, kwargs={
                              "query": query,
                              "bootstrap_servers": bootstrap_servers,
                              "group_id": group_id,
                              "sleep_time": sleep_time,
                              **kwargs
                              })
    thread.start()
    return thread