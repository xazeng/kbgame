# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Lobby(KBEngine.Space):
	def __init__(self):
		KBEngine.Space.__init__(self)
		INFO_MSG("create lobby cell: %d" % (self.gameId))

		# 想根据 gameId 读取房间配置创建房间
		# 可是，引擎不支持了。。。
		# 所以 Lobby 不适合做成 space
		# 应该做成 base entity，人数之类的数值靠客户端主动刷新，不做推送
