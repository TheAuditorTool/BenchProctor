CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp audit_profile.cpp compact_config.cpp directory_sync.cpp format_batch.cpp format_checkpoint.cpp format_receipt.cpp httplib_impl.cpp normalize_threshold.cpp prune_ledger.cpp server_main.cpp
TARGET  = directory_sync

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
