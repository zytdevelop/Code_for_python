import logging

# create logger

module_logger = logging.getLogger('spam_application.auxiliary')


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')

    def do_something(self):
        self.logger.info('doing someting')
        a = 1 + 1
        self.logger.info('done doing something')


def some_function():
    module_logger.info('recevied a call to "some function"')
