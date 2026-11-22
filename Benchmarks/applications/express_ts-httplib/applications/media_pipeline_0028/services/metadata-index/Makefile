CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp enrich_roster.cpp fetch_profile.cpp httplib_impl.cpp load_threshold.cpp metadata_index.cpp resolve_receipt.cpp rotate_receipt.cpp server_main.cpp verify_record.cpp
TARGET  = metadata_index

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
