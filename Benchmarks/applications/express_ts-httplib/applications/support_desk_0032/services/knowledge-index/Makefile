CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -pthread
SOURCES = collect_summary.cpp enrich_digest.cpp httplib_impl.cpp knowledge_search.cpp load_report.cpp rotate_roster.cpp rotate_snapshot.cpp server_main.cpp summarize_checkpoint.cpp
TARGET  = knowledge_search

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
