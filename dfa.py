#!/usr/bin/env python3

import traceback
from abc import ABCMeta, abstractmethod, abstractproperty


class BaseDFA(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        # DFA Statuses
        # A map from status name to status class/callable.
        # Must contains status: start.
        # Mustn't contains status: end.
        self.statuses = None

    def run(self):
        try:
            name = "start"
            while True:
                body = self.statuses.get(name)
                if name == "end":
                    break
                if body is None:
                    print("WARNING: Unknown status name: %s" % name)
                    break
                if isinstance(body, str):
                    name = body
                    continue
                if issubclass(body, BaseDFAStatus):
                    name = body().do()
                elif callable(body):
                    name = body()
        except:
            traceback.print_exception()


class BaseDFAStatus(metaclass=ABCMeta):
    @abstractmethod
    def do(self):
        pass
