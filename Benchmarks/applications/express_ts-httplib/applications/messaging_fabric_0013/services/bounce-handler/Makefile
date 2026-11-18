CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lsqlite3 -pthread
SOURCES = app_db.cpp audit_message.cpp bounce_record.cpp compact_ledger.cpp enrich_header.cpp format_checkpoint.cpp httplib_impl.cpp publish_schedule.cpp render_report.cpp server_main.cpp summarize_schedule.cpp
TARGET  = bounce_record

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
