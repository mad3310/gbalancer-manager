#!/usr/bin/env python
#-*- coding: utf-8 -*-


from handlers.gbalancer import *

handlers = [
            (r"/glb/start", Startgbalancer),
            (r"/glb/stop", Stopgbalancer)
]