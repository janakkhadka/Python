#5.1.2. Using Lists as Queues

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives

queue.append("Graham")          # Graham arrives

print(queue.popleft())