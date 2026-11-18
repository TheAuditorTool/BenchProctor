CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = annotate_report.cpp build_window.cpp compact_window.cpp httplib_impl.cpp presence_track.cpp resolve_receipt.cpp rotate_document.cpp server_main.cpp verify_receipt.cpp
TARGET  = presence_track

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
