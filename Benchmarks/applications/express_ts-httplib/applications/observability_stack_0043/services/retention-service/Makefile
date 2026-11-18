CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp audit_manifest.cpp fetch_window.cpp httplib_impl.cpp load_manifest.cpp prune_alert.cpp prune_config.cpp render_threshold.cpp retention_sweep.cpp server_main.cpp summarize_alert.cpp
TARGET  = retention_sweep

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
