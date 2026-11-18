CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lhiredis -lsqlite3 -pthread
SOURCES = annotate_report.cpp app_db.cpp audit_batch.cpp enrich_delivery.cpp enrich_record.cpp export_bundle.cpp fetch_bundle.cpp httplib_impl.cpp normalize_record.cpp presence_update.cpp server_main.cpp
TARGET  = presence_update

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
