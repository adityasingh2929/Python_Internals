'''

1. Python is an interpreted language:
    -> It runs line by line     = Not fully true 
    -> Python execution Pipeline:
        .py source code
            | (our code is compiled into bytecode by the CPython compiler (which's inside the interpreter).)
        tokens  (smallest meaningful pieces of the code, each token has a type and a value)
            |
        AST     (Tokens alone are not enough, we need to answer the relation btw the tokens  -> AST is a tree that explains what the code means, not how it looks   | AST organizes tokens into a structure)   | Syntax Errors happen at this AST Stage. Python fails before execution because tokens exist but AST (relation btw tokens) cannot be built.
            |
        Bytecode (.pyc extension if its cached by python)
            | 
        Python Virtual Machine (PVM) [interpreter loop]
            |
        CPU

        explaination: Python source code is converted into python bytecode and then the bytecode is fed to the PVM (which is a pre-compiled/pre-written machine code [in C] that was written using CPython), our CPU runs the machine..and that machine basically takes the instructions from the bytecode file and executes them line by line by deciding which branch (execution flow) of it'll be executed (according to the instructions) and hence not all the python files have the same execution path despite having the same PVM.

        The second run will always be faster if the python caches the bytecode file of our source code into __pycache__/  (which results in the '.pyc' extension)

        The execution happens instruction by instruction of the bytecode file, note line by line for python source code (as one python source code's line can have multiple isntructions, or sometimes none).

'''

# shows the SourceCode-ByteCode

import dis

def functions():
    x = 1
    y = 2
    return x+y

dis.dis(functions)   


# Detailed process of SourceCode to ByteCode: 
#   source code -> tokens

import tokenize 
from io import BytesIO

code = b"x = 1 + 2"
for tok in tokenize.tokenize(BytesIO(code).readline):
    print(tok)


# Detailed process of SourceCode to ByteCode:
#   tokens -> AST

import ast 

tree = ast.parse("x = 1 + 1")
print(ast.dump(tree,indent=4))      
# Example: x = 1+2*3    | main tokens: x,-,1,+,*,3, etc.   | AST adds meaning that '*' happens before '+'. AST doesnt care about spaces,comments,formatting,useless parenthesis.


# IMP INFORMATION:
'''
    
'''


# Proving that the Runtime Errors happen during Execution:

def h():
    print("Start")
    # x = 1 / 0
    print("End")

h()

# "Start" gets printed but then the crash occurs before printing "End". This tells us that Bytecode gets executed sequentially (instructions gets executed one by one) by the PVM when the CPU executes the PVM and its fed the ByteCode (data which is basically our SourceCode).
#   x = 1 + 2   -> has multiple bytecode instructions (load_fast,binary_op,store_fast).
#   return 42   (or another example)  pass -> these 2 have only one bytecode instruction.
#  a comment has 0 bytecode instructions.


# Cached compiled (bytecode) files
    # run the file normally, check for __pycache__/ folder as it'll be created in the same directory of your executed file, it'll store the .pyc of your source code file if the file is cached.
    # The file will appear in the pycache folder when its being used in another file (i.e being imported).