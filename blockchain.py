from block import Block
import datetime

block_chain = [Block.create_genesis_block()]

print("hash %s" % block_chain[-1].hash)

to_add = 10

for _ in range(1, to_add):
    block_chain.append(Block(block_chain[-1].hash,
                             "DATA!", datetime.datetime.now()))
    print("Block #%d hash %s" % (_, block_chain[_].hash))
