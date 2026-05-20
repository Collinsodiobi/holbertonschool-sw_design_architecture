#!/usr/bin/env python3


class NewsSubject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        self._observers = [
            (obs, topics)
            for obs, topics in self._observers
            if obs != observer
        ]

    def notify(self, topic, data):
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()

    log_observer = LogObserver()
    email_observer = EmailObserver()
    sms_observer = SmsObserver()

    subject.subscribe(log_observer, {"sports", "breaking"})
    subject.subscribe(email_observer)
    subject.subscribe(sms_observer, {"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
