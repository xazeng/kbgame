# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Lobby(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		self.gameId = self.cellData["gameId"]
		INFO_MSG("create lobby base: %d" % (self.gameId))

	def onGetCell(self):
		INFO_MSG("onGetCell")
		
		# 根据self.gameId 去找配置, 然后创建 room
		# 也可以直接在 __init__ 里面创建

		self.rooms = {}
		self.rooms[20001] = KBEngine.createEntityAnywhere("Room", {"gameId":self.gameId, "roomId":20001})

		