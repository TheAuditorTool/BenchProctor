CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp audit_bundle.cpp collect_checkpoint.cpp enrich_roster.cpp export_header.cpp httplib_impl.cpp load_metric.cpp render_schedule.cpp sample_config.cpp server_main.cpp
TARGET  = sample_config

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
