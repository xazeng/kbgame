# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Lobby(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		self.gameId = self.cellData["gameId"]
		KBEngine.globalData["lobby_" + str(self.gameId)] = self
		INFO_MSG("create lobby base: %d" % (self.gameId))

	def onCreateRoom(self, entityCall, roomId):
		self.rooms[roomId] = entityCall 

	def onGetCell(self):
		# 根据self.gameId 去找配置, 然后创建 room
		# 也可以直接在 __init__ 里面创建
		self.rooms = {}
		KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20001}, lambda x:self.onCreateRoom(x, 20001))
		KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20002}, lambda x:self.onCreateRoom(x, 20002))
		KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20003}, lambda x:self.onCreateRoom(x, 20003))
		KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20004}, lambda x:self.onCreateRoom(x, 20004))
		KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20005}, lambda x:self.onCreateRoom(x, 20005))
		KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20006}, lambda x:self.onCreateRoom(x, 20006))

		