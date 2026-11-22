CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp build_checkpoint.cpp collect_ledger.cpp collect_report.cpp compact_config.cpp fetch_window.cpp httplib_impl.cpp normalize_digest.cpp render_roster.cpp server_main.cpp shipment_quote.cpp
TARGET  = shipment_quote

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
