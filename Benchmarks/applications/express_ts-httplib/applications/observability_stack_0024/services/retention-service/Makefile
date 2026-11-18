CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp audit_bundle.cpp enrich_window.cpp export_summary.cpp httplib_impl.cpp load_window.cpp reconcile_report.cpp retention_sweep.cpp rotate_digest.cpp server_main.cpp
TARGET  = retention_sweep

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
