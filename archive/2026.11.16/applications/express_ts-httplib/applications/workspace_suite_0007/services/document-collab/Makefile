CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp build_index.cpp document_edit.cpp enrich_digest.cpp httplib_impl.cpp load_record.cpp load_roster.cpp load_summary.cpp render_checkpoint.cpp server_main.cpp summarize_digest.cpp
TARGET  = document_edit

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
