CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp enrich_threshold.cpp fetch_window.cpp format_record.cpp httplib_impl.cpp knowledge_search.cpp load_ledger.cpp render_ticket.cpp server_main.cpp summarize_checkpoint.cpp summarize_receipt.cpp
TARGET  = knowledge_search

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
