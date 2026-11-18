CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = annotate_profile.cpp app_db.cpp archive_schedule.cpp compact_flag.cpp enrich_digest.cpp fetch_batch.cpp httplib_impl.cpp server_main.cpp tenant_provision.cpp validate_bundle.cpp verify_digest.cpp
TARGET  = tenant_provision

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
