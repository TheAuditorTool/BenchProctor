CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lsqlite3 -pthread
SOURCES = app_db.cpp export_config.cpp httplib_impl.cpp knowledge_search.cpp merge_index.cpp merge_ledger.cpp normalize_report.cpp reconcile_batch.cpp reconcile_receipt.cpp server_main.cpp
TARGET  = knowledge_search

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
