CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -pthread
SOURCES = build_ledger.cpp collect_header.cpp export_rule.cpp fetch_bundle.cpp httplib_impl.cpp merge_rule.cpp reconcile_checkpoint.cpp reconcile_decision.cpp server_main.cpp watchlist_sync.cpp
TARGET  = watchlist_sync

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
