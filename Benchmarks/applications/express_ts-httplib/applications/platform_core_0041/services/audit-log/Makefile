CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -pthread
SOURCES = annotate_secret.cpp audit_append.cpp build_index.cpp compact_flag.cpp export_flag.cpp fetch_summary.cpp httplib_impl.cpp load_header.cpp resolve_index.cpp server_main.cpp
TARGET  = audit_append

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
