import time
from merkletools import MerkleTools

_difficult = 30
entry_list = [
  "abababababababab",
  "gtgtgtgtgtgtggtg",
  "jukikiklilillill",
  "popopuiupipupipu"
]


class BlockMining:
    def __init__(self, series_of_transaction):
        self.series_of_transaction = series_of_transaction
        self.hash_result = self.make_tree(entry_list).get_merkle_root()

    @staticmethod
    def make_tree(hash_to_tree):
        mt = MerkleTools(hash_type="sha256")
        mt.add_leaf(hash_to_tree, True)
        mt.make_tree()
        return mt

    def proof_of_work(self, header, difficulty_bits):
        target_val = 2 ** (256-difficulty_bits)

        for nonce in range(2 ** _difficult):
            hash_result = self.make_tree(header+str(nonce)).get_merkle_root()
            if int(hash_result, 16) < target_val:
                print("Hash: %s" % hash_result)
                print("Success nonce %d" % nonce)
                return hash_result, nonce
        print("Failed after %d (max_nonce) nonces" % nonce)
        return nonce


def main():
    result = BlockMining(entry_list)

    for difficulty_bits in range(_difficult):
        print("Difficulty: %ld (%d bits)" % (2 ** difficulty_bits, difficulty_bits))

        print("Starting search...\n\n")
        start_time = time.time()

        new_block = 'Oto transakcja' + result.hash_result
        print("Last block:" + result.hash_result)

        result.hash_result, nonce = result.proof_of_work(new_block, difficulty_bits)

        print("Elapsed Time Of Mining: %.4f seconds" % (time.time() - start_time))


if __name__ == '__main__':
    main()
