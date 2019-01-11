import sys
sys.path.append("C:/Users/xiao0/projects_pro")
from ex14.ex14.ex14 import DLList

class Dictionary(object):

    def __init__(self, buckets=256):
        self.map = DLList()
        for i in range(0, buckets):
            self.map.push(DLList())

    def hash_key(self, key):
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)

    def get_slot(self, key):
        bucket = self.get_bucket(key)
        slot = bucket.begin

        while slot:
            if slot.value[0] == key:
                return bucket, slot
            else:
                slot = slot.next

        return bucket, None

    def set(self, key, value):
        bucket, slot = self.get_slot(key)
        if slot:
            slot.value = (key, value)
        else:
            bucket.push((key, value))

    def get(self, key, default='default'):
        bucket, slot = self.get_slot(key)
        if slot:
            return slot.value[1]
        else:
            return None

    def delete(self, key):
        bucket, slot = self.get_slot(key)
        if slot:
            bucket.detach_node(slot)

    def list(self):
        bucket = self.map.begin
        while bucket:
            slot = bucket.value.begin
            while slot:
                print(slot.value)
                slot = slot.next
            bucket = bucket.next