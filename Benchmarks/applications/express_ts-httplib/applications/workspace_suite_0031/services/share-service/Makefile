CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lrabbitmq -lsqlite3 -pthread
SOURCES = annotate_ledger.cpp app_db.cpp archive_snapshot.cpp compact_manifest.cpp format_record.cpp httplib_impl.cpp load_receipt.cpp normalize_policy.cpp server_main.cpp share_grant.cpp
TARGET  = share_grant

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
