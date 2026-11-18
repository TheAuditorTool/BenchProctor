CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lpq -pthread
SOURCES = archive_profile.cpp compact_index.cpp enrich_index.cpp httplib_impl.cpp reconcile_record.cpp server_main.cpp sku_lookup.cpp validate_batch.cpp validate_roster.cpp
TARGET  = sku_lookup

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
