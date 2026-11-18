CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp archive_mapping.cpp collect_connector.cpp fetch_ledger.cpp fetch_record.cpp field_mapping.cpp format_roster.cpp httplib_impl.cpp publish_summary.cpp server_main.cpp
TARGET  = field_mapping

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
