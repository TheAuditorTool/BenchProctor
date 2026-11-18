CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp archive_connector.cpp collect_digest.cpp connector_invoke.cpp format_digest.cpp format_policy.cpp httplib_impl.cpp load_batch.cpp normalize_window.cpp resolve_mapping.cpp server_main.cpp
TARGET  = connector_invoke

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
