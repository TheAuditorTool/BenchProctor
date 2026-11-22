CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp audit_ledger.cpp audit_roster.cpp collect_label.cpp enrich_index.cpp format_batch.cpp httplib_impl.cpp merge_roster.cpp publish_report.cpp server_main.cpp shipment_quote.cpp
TARGET  = shipment_quote

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
