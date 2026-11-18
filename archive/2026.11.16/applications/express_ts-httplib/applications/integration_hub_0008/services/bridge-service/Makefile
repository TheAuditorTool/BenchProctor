CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp export_schedule.cpp httplib_impl.cpp queue_bridge.cpp reconcile_manifest.cpp render_manifest.cpp resolve_schedule.cpp rotate_batch.cpp server_main.cpp validate_roster.cpp
TARGET  = queue_bridge

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
