from software.FileSystem import *
from software.Scheduler import *
from software.Kernel import *

from hardware.MMU import *
from hardware.Clock import *
from hardware.CPU import *
from hardware.Memory import *
from hardware.Queues import *

instructionAdd = Instruction(True, "add")
instructionIO = Instruction(False, "IO")
instructionEND = Instruction(True, "end")

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
fileSystem.addProgram(program0)
fileSystem.addProgram(program1)
fileSystem.addProgram(program2)
fileSystem.addProgram(program3)

memory = Memory(4)
mmu = MMU(memory)

# startQueue = StartQueue()
# ioQueue = IOQueue()

readyQueue = ReadyQueue()
cpu = CPU(mmu)
clock = Clock(cpu)

scheduler = Scheduler()
kernel = Kernel(cpu, scheduler, mmu)
kernel.start()
