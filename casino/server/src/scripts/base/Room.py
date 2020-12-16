# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Room(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		self.gameId = self.cellData["gameId"]
		self.roomId = self.cellData["roomId"]
		INFO_MSG("create room base: gameId = %d, roomId = %d" % (self.gameId, self.roomId))

