#705. Design HashSet
''' 
- First of all, I've taken bucket, bucketItems and storage. 
- It consists of 1000 buckets, each capable of holding 1000 items, managed by the self.storage list. 
- The add() method adds an element to the HashSet by calculating the bucket and bucket item index, then marking its presence with True. 
- The remove() method removes an element by marking its corresponding item as None, and the contains() method checks if an element exists by verifying the presence of True in the relevant item. '''
class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.bucketItems = 1000
        self.storage = [None]*self.buckets

    def getBucket(self,key:int)->int:
        return key % self.buckets

    def getBucketItems(self,key:int)->int:
        return key // self.bucketItems

    def add(self, key: int) -> None:
        bucket = self.getBucket(key)
        bucketItem = self.getBucketItems(key)
        if self.storage[bucket] == None:
            if bucket ==0:
                self.storage[bucket]= [None]*(self.bucketItems+1)
            else:
                self.storage[bucket] = [None]* self.bucketItems
        
        self.storage[bucket][bucketItem] = True

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        bucketItem = self.getBucketItems(key)

        if self.storage[bucket] == None:
            return
        self.storage[bucket][bucketItem] = None
        

    def contains(self, key: int) -> bool:
        bucket = self.getBucket(key)
        bucketItem = self.getBucketItems(key)
        if self.storage[bucket]==None:
            return False
        return  self.storage[bucket][bucketItem] == True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
