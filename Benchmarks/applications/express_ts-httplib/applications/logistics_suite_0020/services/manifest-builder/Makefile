CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp build_checkpoint.cpp compact_receipt.cpp httplib_impl.cpp manifest_build.cpp merge_header.cpp normalize_bundle.cpp prune_manifest.cpp server_main.cpp verify_threshold.cpp
TARGET  = manifest_build

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
