# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Lobby(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		if not KBEngine.globalData.__contains__("lobbys"):
			KBEngine.globalData["lobbys"] = {}
		self.gameId = self.cellData["gameId"]
		INFO_MSG("create lobby base: %d" % (self.gameId))
		KBEngine.globalData["lobbys"][self.cellData["gameId"]] = self

	def onGetCell(self):
		INFO_MSG("onGetCell")
		
		# 根据配置创建 room

		self.rooms = {}
		self.rooms[20001] = KBEngine.createEntityAnyWhere("Room", {"gameId":self.gameId, "roomId":20001})

		