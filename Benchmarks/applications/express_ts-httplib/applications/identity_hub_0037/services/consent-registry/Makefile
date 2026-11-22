CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp audit_digest.cpp collect_snapshot.cpp consent_record.cpp enrich_config.cpp httplib_impl.cpp merge_policy.cpp prune_policy.cpp server_main.cpp summarize_schedule.cpp validate_manifest.cpp
TARGET  = consent_record

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
