CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = annotate_snapshot.cpp app_db.cpp archive_policy.cpp audit_threshold.cpp enrich_schedule.cpp fetch_record.cpp httplib_impl.cpp payment_authorize.cpp server_main.cpp summarize_threshold.cpp
TARGET  = payment_authorize

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
