compressed stream / decompresscat
---------------------------------

A simple python module and utility to handle streams of compressed files.

## decompresscat

```text
usage: decompresscat [-h] [--algorithm {gz,bz2,7z,lzma}] [--quiet] [--csv]
                     FILE [FILE ...]

decompresses files to stdout

positional arguments:
  FILE                  File to decompress.

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {gz,bz2,7z,lzma}, -a {gz,bz2,7z,lzma}
                        Force decompression algorithm instead of using file
                        extension.
  --quiet, -q           Don't write any output
  --csv                 Read file with CSV reader
```

##  decompressgrep

**This function has not been implemented yet**

```text
usage: decompressgrep [-h] [--algorithm {gz,bz2,7z,lzma}] [--quiet] [--csv]
                      FILE [FILE ...]

search possibly compressed files for a regular expression

positional arguments:
  FILE                  File to decompress.

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {gz,bz2,7z,lzma}, -a {gz,bz2,7z,lzma}
                        Force decompression algorithm instead of using file
                        extension.
  --quiet, -q           Don't write any output
  --csv                 Read file with CSV reader
```

## decompressdiff, decompresscmp

**This function has not been implemented yet**

```text
usage: decompressdiff, decompresscmp [-h] [--algorithm {gz,bz2,7z,lzma}]
                                     [--quiet] [--csv]
                                     FILE [FILE ...]

compare compressed files

positional arguments:
  FILE                  File to decompress.

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {gz,bz2,7z,lzma}, -a {gz,bz2,7z,lzma}
                        Force decompression algorithm instead of using file
                        extension.
  --quiet, -q           Don't write any output
  --csv                 Read file with CSV reader
```

## decompressless

**This function has not been implemented yet**

```text
usage: decompressless [-h] [--algorithm {gz,bz2,7z,lzma}] [--quiet] [--csv]
                      FILE [FILE ...]

file perusal filter for viewing of compressed text

positional arguments:
  FILE                  File to decompress.

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {gz,bz2,7z,lzma}, -a {gz,bz2,7z,lzma}
                        Force decompression algorithm instead of using file
                        extension.
  --quiet, -q           Don't write any output
  --csv                 Read file with CSV reader
```

## decompressmore


**This function has not been implemented yet**

```text
usage: decompressmore [-h] [--algorithm {gz,bz2,7z,lzma}] [--quiet] [--csv]
                      FILE [FILE ...]

file perusal filter for viewing of compressed text

positional arguments:
  FILE                  File to decompress.

optional arguments:
  -h, --help            show this help message and exit
  --algorithm {gz,bz2,7z,lzma}, -a {gz,bz2,7z,lzma}
                        Force decompression algorithm instead of using file
                        extension.
  --quiet, -q           Don't write any output
  --csv                 Read file with CSV reader
```
