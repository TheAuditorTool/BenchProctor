CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = annotate_snapshot.cpp app_db.cpp enrich_receipt.cpp enrich_summary.cpp export_config.cpp httplib_impl.cpp load_receipt.cpp presence_update.cpp server_main.cpp validate_report.cpp
TARGET  = presence_update

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
