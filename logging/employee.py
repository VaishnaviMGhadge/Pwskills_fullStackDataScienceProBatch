#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')
file_handler=logging.FileHandler('employe_detail.log')
file_handler.setFormatter(formatter)
logger.addHandler((file_handler))


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info("name of employee is {} and email is {}".format(self.fulname, self.email))

    @property
    def email(self):
        return "{}{}@gmail.com".format(self.first, self.last)

    @property
    def fulname(self):
        return "{} {} ".format(self.first, self.last)

e1=Employee("shreya","ghadge")

