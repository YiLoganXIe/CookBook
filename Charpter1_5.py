# Created by Yi Xie 6/30/2019
# This is an example from PythonCookbook
# This example is a implementation of Priority Queue in Python

import heapq


class PriorityQueue:
    def __init__(self):
        self.m_queue = []
        self.m_size = 0

    def push_queue(self, item, priority):
        heapq.heappush(self.m_queue, (-priority, self.m_size, item))
        self.m_size += 1

    def pop_queue(self):
        return heapq.heappop(self.m_queue)



