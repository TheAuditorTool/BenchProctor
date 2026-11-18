CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp enrich_reservation.cpp httplib_impl.cpp load_roster.cpp merge_summary.cpp publish_bundle.cpp reconcile_receipt.cpp server_main.cpp summarize_header.cpp supplier_feed.cpp
TARGET  = supplier_feed

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
