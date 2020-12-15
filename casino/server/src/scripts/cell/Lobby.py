# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Lobby(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		INFO_MSG("create lobby cell: %d" % (self.gameId))

		# 根据 gameId 读取房间配置创建房间
		# 到这里，引擎不支持了。。。
