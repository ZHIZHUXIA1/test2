import random

from signalslot import Signal
from ControlBase import CtrlBase
from ViewBase import ViewBase
from ReadModbusTcp import ReadModbusTcp
import time


class MyCtrl(CtrlBase, ReadModbusTcp):
    def __init__(self):
        self.signal = Signal()

    def run(self, kwargs):
        while True:
            iTActor = {"interActor": kwargs["interActor"]}
            lst = self.dictreadtag
            lst1 = self.dictreadtag1
            pos = {"pos": lst, "pos1": lst1}
            self.signal.emit(**pos, **iTActor)
            time.sleep(1)


class MyView(ViewBase):
    def set_mvc_control(self, ctrl):
        super().set_mvc_control(ctrl)
        ctrl.signal.connect(self.slot_a)

    def slot_a(self, **kwargs):
        pass
