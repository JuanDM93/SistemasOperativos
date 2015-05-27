from software.Program import *
from software.MMU import *
from software.FileSystem import *

from hardware.Clock import *
from hardware.CPU import *
from hardware.Memory import *
from hardware.Queues import *

instructionAdd = Instruction(True, "add")
instructionIO = Instruction(False, "IO")
instructionEND = Instruction(False, "end")

instructionSet0 = (instructionAdd, instructionAdd, instructionIO, instructionAdd,
                   instructionAdd, instructionEND)
instructionSet1 = (instructionAdd, instructionIO, instructionAdd, instructionIO,
                   instructionEND)
instructionSet2 = (instructionIO, instructionAdd, instructionEND)
instructionSet3 = (instructionAdd, instructionIO, instructionEND)

program0 = Program("pacman", instructionSet0)
program1 = Program("gato", instructionSet1)
program2 = Program("tetris", instructionSet2)
program3 = Program("space", instructionSet3)

disk = Disk(64)
fileSystem = FileSystem(disk)
memory = Memory(4)
mmu = MMU(memory)

# startQueue = ReadyQueue()
# ioQueue = ReadyQueue()

readyQueue = ReadyQueue()
cpu = CPU(mmu)
clock = Clock(cpu)

# scheduler = Scheduler(2)
