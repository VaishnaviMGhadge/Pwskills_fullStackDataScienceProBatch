
import logging

import employee
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler=logging.FileHandler('calculator.log')
file_handler.setFormatter(formatter)
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler((file_handler))
logger.addHandler((stream_handler))


def add(a, b):
    logger.info("addition")
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b

num1=10
num2=2

add_numbers=add(num1,num2)

logger.debug("addition of number is=%d",add_numbers)

sub_numbers=sub(num1,num2)
logger.debug("substraction of number is=%d",sub_numbers)

mul_numbers=mul(num1,num2)
logger.debug("multiplication of numbers is=%d",mul_numbers)
