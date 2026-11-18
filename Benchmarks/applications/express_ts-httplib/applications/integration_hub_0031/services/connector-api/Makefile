CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp connector_invoke.cpp export_policy.cpp export_window.cpp format_header.cpp httplib_impl.cpp reconcile_snapshot.cpp render_config.cpp server_main.cpp summarize_batch.cpp validate_webhook.cpp
TARGET  = connector_invoke

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
