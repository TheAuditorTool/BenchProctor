CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lsqlite3 -pthread
SOURCES = app_db.cpp audit_checkpoint.cpp collect_manifest.cpp fetch_mandate.cpp httplib_impl.cpp merge_digest.cpp merge_index.cpp payout_schedule.cpp publish_receipt.cpp rotate_config.cpp server_main.cpp
TARGET  = payout_schedule

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
