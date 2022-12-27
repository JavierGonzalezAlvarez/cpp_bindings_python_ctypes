# bindings with python - ctypes

## virtual environment
$ virtualenv entorno_virtual -p python3.11

## Activar entorno virtual
$ source entorno_virtual/bin/activate

## compile library
$ g++ -c -o libsum.o libsum.cpp
best option:
$ g++ -c -o libsum.o libsum.cpp -fPIC

## create a static library
$ ar rcs libsum.a libsum.o
$ ar cr libsum.a libsum.o

## create a shared library .so
$ g++ -shared -o libsum.so libsum.o

## run c++
./libsum

## run python
python3 main.py
