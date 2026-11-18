CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp enrich_threshold.cpp fetch_window.cpp format_manifest.cpp httplib_impl.cpp load_policy.cpp merge_index.cpp prune_digest.cpp prune_ledger.cpp server_main.cpp transcode_job.cpp
TARGET  = transcode_job

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
