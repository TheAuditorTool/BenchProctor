CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = annotate_device.cpp app_db.cpp archive_ledger.cpp httplib_impl.cpp normalize_threshold.cpp reconcile_roster.cpp render_config.cpp server_main.cpp session_create.cpp summarize_batch.cpp
TARGET  = session_create

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
