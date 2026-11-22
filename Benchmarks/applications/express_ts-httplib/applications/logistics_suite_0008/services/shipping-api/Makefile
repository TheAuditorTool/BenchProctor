CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp build_snapshot.cpp fetch_policy.cpp format_report.cpp httplib_impl.cpp merge_batch.cpp publish_ledger.cpp server_main.cpp shipment_quote.cpp verify_threshold.cpp
TARGET  = shipment_quote

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
