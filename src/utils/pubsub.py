class PubSub:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.subscribers:
            if callback in self.subscribers[event]:
                self.subscribers[event].remove(callback)

    def publish(self, event, *args, **kwargs):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(*args, **kwargs)
