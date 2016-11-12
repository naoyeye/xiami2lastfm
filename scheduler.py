# -*- coding: utf-8 -*-
# @Author: hanjiyun
# @Date:   2016-11-13 02:04:24
# @Last Modified by:   hanjiyun
# @Last Modified time: 2016-11-13 02:05:15

from threading import Timer, Thread
from time import sleep


class Scheduler(object):
  def __init__(self, sleep_time, function):
    self.sleep_time = sleep_time
    self.function = function
    self._t = None

  def start(self):
    if self._t is None:
      self._t = Timer(self.sleep_time, self._run)
      self._t.start()
    else:
      raise Exception("this timer is already running")

  def _run(self):
    self.function()
    self._t = Timer(self.sleep_time, self._run)
    self._t.start()

  def stop(self):
    if self._t is not None:
      self._t.cancel()
      self._t = None