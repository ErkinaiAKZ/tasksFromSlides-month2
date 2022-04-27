
class Queue:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Queue.__instance = None
        del self

    def __init__(self, get_house):
        self.get_house = get_house

    def house(self):
        print(self.get_house, 'got а house')

customer1 = Queue('First customer:')
print(customer1.__dict__)
customer1.house()

customer2 = Queue('Second customer:')
print(customer2.__dict__)
customer2.house()

print(id(customer1), id(customer2))

#Версия с использованием библиотеки:

# from collections import deque
#
# class Queue:
#     def __init__(self):
#         self.items = deque()
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         return self.items.popleft()
#
#     def get_foremost_data(self):
#         return self.items[0]
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size_of_queue(self):
#         return len(self.items)
#
#     def __str__(self):
#         return str(self.items)
#
# q = Queue()
# print(q)
# print(q.is_empty())
#
# q.enqueue("Клиент1")
# q.enqueue("Клиент2")
# q.enqueue("Клиент3")
#
# print(q)
#
# q.dequeue()
# print(q)
#
# print("Текущая длина очереди:", q.size_of_queue())
#
# print("Первый в очереди:", q.get_foremost_data())
# q.dequeue()
# print("Первый в очереди:", q.get_foremost_data())