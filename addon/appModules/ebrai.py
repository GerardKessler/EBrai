# -*- coding: utf-8 -*-
# Copyright (C) 2021 Gerardo Kessler <ReaperYOtrasYerbas@gmail.com>
# This file is covered by the GNU General Public License.

import appModuleHandler
from scriptHandler import script
import api
from re import search
from ui import message

class AppModule(appModuleHandler.AppModule):

	@script(gesture="kb:control+shift+e")
	def script_positionAnnounce(self, gesture):
		obj = api.getForegroundObject().children[1].children[6].children[4].name
		message(obj)

	@script(gesture="kb:control+shift+c")
	def script_columnAnnounce(self, gesture):
		obj = api.getForegroundObject().children[1].children[6].children[4].name
		columnas = search(r"Columna.{2,4}\d{1,2}", obj)
		message(columnas[0])
