CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp compact_digest.cpp compact_index.cpp fetch_config.cpp fetch_index.cpp httplib_impl.cpp publish_summary.cpp reconcile_index.cpp redaction_apply.cpp server_main.cpp summarize_record.cpp
TARGET  = redaction_apply

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
