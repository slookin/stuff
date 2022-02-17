from lark import Lark, logger
import logging
import os
import time

logger.setLevel(logging.DEBUG)

dir_path = os.path.dirname(os.path.realpath(__file__))
grammar_file_path = os.path.join(dir_path, "puml_sequence_demo.ebnf")
f = open(grammar_file_path)
l = Lark(f.read())
f.close()
logger.debug("grammar loaded")


example_file_path = os.path.join(dir_path, "test.puml")
f = open(example_file_path)
start_time = time.time()
logger.debug("parsing...")
result = l.parse(f.read())
logger.debug("parsing end")
logger.debug("--- %s seconds ---" % (time.time() - start_time))
f.close()
print(result)
print(result.pretty())
