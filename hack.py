# by @f0rizen

from .. import loader, utils

import logging
import asyncio
import time

logger = logging.getLogger(__name__)

@loader.tds
class HACKMod(loader.Module):
	"""Hack your ass"""
	strings = {"name": "Hack"}
	def __init__(self):
		self.name = self.strings["name"]
	def config_complete(self):
		pass
	async def hackcmd(self, message):
		"""Hack your ass"""
		i = 0
		while i <= 100:
			await message.edit("Ass hacked for " + str(i) + "%")
			i += 1
			time.sleep(0.3)
		await message.edit("Ass successfully hacked")
		return

