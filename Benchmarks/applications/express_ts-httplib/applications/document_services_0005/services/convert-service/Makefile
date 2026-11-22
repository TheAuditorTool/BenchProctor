CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp build_roster.cpp collect_batch.cpp compact_config.cpp compact_signature.cpp convert_job.cpp format_schedule.cpp httplib_impl.cpp publish_header.cpp server_main.cpp summarize_threshold.cpp
TARGET  = convert_job

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
