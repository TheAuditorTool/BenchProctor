CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp audit_ledger.cpp httplib_impl.cpp merge_config.cpp normalize_checkpoint.cpp prune_partner.cpp publish_summary.cpp retry_queue.cpp server_main.cpp validate_connector.cpp
TARGET  = retry_queue

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
