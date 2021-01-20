# Compression
Fun with compression

Here's a couple of compression algorithms I wrote. 

There are three different compression techniques used: Delta Compression, LZSS Compression, and Huffman Encoding.

LZSS is the best of the algorithms. It uses a technique similar to how ZIP files are compressed. If given a well formed file, it can beat the ZIP compression algorithms, although on average it is slightly worse, but very close to zipped files in size.

I'm still working on the huffman and delta encodings, so they currently work, but are not nearly at max efficency.
