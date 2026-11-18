CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp audit_window.cpp collect_window.cpp enrich_schedule.cpp httplib_impl.cpp reconcile_record.cpp screening_run.cpp server_main.cpp validate_manifest.cpp validate_receipt.cpp verify_index.cpp
TARGET  = screening_run

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
