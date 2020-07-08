from kafka import KafkaConsumer
from kafka import TopicPartition
from kafka import OffsetAndMetadata

import time
import threading


def start_commiter(query, bootstrap_servers, group_id, sleep_time=5, **kwargs):
    options = {
        "auto_offset_reset": "earliest",
        "bootstrap_servers": bootstrap_servers,
        "group_id": group_id,
        "api_version": "2.4.0",
        **kwargs
    }

    consumer = KafkaConsumer(**options)
    time.sleep(5)

    while query.isActive:
        for offsets in query.lastProgress['sources']:
            end_offsets = offsets['endOffset']
            for topic in end_offsets.keys():
                for partition in end_offsets[topic].keys():
                    offset = end_offsets[topic][partition]
                    topic_partition = TopicPartition(topic, int(partition))
                    consumer.assign([topic_partition])
                    consumer.commit(
                        {topic_partition: OffsetAndMetadata(offset, None)})
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
