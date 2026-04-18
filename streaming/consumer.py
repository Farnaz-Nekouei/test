from collections import deque

buffer = deque(maxlen=200)

def consume(stream):
    for event in stream:
        buffer.append(event)
    return buffer