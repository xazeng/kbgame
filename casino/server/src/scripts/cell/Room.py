# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Room(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		INFO_MSG("create room cell: gameId = %d, roomId = %d" % (self.gameId, self.roomId))
