CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = compact_revision.cpp compact_roster.cpp enrich_summary.cpp enrich_threshold.cpp export_config.cpp fetch_taxonomy.cpp httplib_impl.cpp merge_header.cpp server_main.cpp syndication_push.cpp
TARGET  = syndication_push

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
