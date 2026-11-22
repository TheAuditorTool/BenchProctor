CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lhiredis -lsqlite3 -pthread
SOURCES = app_db.cpp archive_summary.cpp audit_secret.cpp collect_header.cpp export_schedule.cpp httplib_impl.cpp publish_threshold.cpp quota_enforce.cpp server_main.cpp summarize_window.cpp
TARGET  = quota_enforce

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
