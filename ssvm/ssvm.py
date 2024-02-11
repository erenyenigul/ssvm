import plistlib, os
from ir import SSVMIR
from compiler import Compiler

ir = SSVMIR()

ir.action("com.apple.reminders.create")
ir.name = ""

compiler = Compiler("ios17")
compiler.compile("out.plist", ir)