# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Lobby(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		if not KBEngine.globalData.__contains__("lobbys"):
			KBEngine.globalData["lobbys"] = {}
		INFO_MSG("create lobby base: %d" % (self.cellData["gameId"]))
		KBEngine.globalData["lobbys"][self.cellData["gameId"]] = self