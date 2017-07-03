all : libshallowale.so

tiles.o: tiles.cpp
	$(CXX) $(FLAGS) -c -fPIC tiles.cpp

libshallowale.so: tiles.o
	 $(CXX) -shared -Wl,-soname,libtilecoding.so -o libtilecoding.so tiles.o

clean:
	rm -rf ${OUT_FILE} *.o
	rm -f *.so
