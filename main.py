import heapq
from collections import defaultdict, Counter

def create_huffman_tree(freqs):
    heap = [[weight, [symbol, ""]] for symbol, weight in freqs.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0]

def create_huffman_dict(huffman_tree):
    huff_dict = {}
    for pair in huffman_tree[1:]:
        symbol, code = pair
        huff_dict[symbol] = code
    return huff_dict

def huffman_encode(data, huff_dict):
    return "".join(huff_dict[symbol] for symbol in data)

def huffman_decode(encoded_data, huff_dict):
    inv_dict = {code: symbol for symbol, code in huff_dict.items()}
    symbol = ""
    decoded_data = []
    for bit in encoded_data:
        symbol += bit
        if symbol in inv_dict:
            decoded_data.append(inv_dict[symbol])
            symbol = ""
    return "".join(decoded_data)

data = "The quick brown fox jumps over the lazy dog"
freqs = Counter(data)
huffman_tree = create_huffman_tree(freqs)
huff_dict = create_huffman_dict(huffman_tree)

encoded_data = huffman_encode(data, huff_dict)
decoded_data = huffman_decode(encoded_data, huff_dict)

print(f"Original data: {data}")
print(f"Encoded data: {encoded_data}")
print(f"Decoded data: {decoded_data}")
