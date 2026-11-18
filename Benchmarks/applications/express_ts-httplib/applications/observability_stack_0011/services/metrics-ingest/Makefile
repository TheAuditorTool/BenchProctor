CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp export_digest.cpp format_header.cpp httplib_impl.cpp metric_ingest.cpp normalize_config.cpp normalize_index.cpp publish_checkpoint.cpp server_main.cpp summarize_digest.cpp summarize_trace.cpp
TARGET  = metric_ingest

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
