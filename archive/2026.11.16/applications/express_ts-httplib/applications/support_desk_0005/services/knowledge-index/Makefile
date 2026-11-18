CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp archive_threshold.cpp audit_summary.cpp build_ledger.cpp collect_summary.cpp httplib_impl.cpp knowledge_search.cpp reconcile_profile.cpp resolve_roster.cpp server_main.cpp
TARGET  = knowledge_search

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
