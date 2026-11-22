CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp compact_batch.cpp enrich_receipt.cpp httplib_impl.cpp load_batch.cpp merge_receipt.cpp normalize_trace.cpp render_manifest.cpp retention_sweep.cpp server_main.cpp summarize_manifest.cpp
TARGET  = retention_sweep

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
