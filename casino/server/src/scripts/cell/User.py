# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class User(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		INFO_MSG("create user cell")