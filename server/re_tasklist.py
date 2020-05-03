#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/29 --

import os
from distutils.log import warn as printf
import re

# unix use who
# window use tasklist
with os.popen('tasklist', 'r') as f:
    for each_line in f:
        printf(re.split(r'\s\s+|\t', each_line.strip()))
