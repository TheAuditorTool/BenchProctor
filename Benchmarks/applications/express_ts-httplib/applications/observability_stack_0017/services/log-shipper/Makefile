CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp compact_config.cpp httplib_impl.cpp load_record.cpp log_ship.cpp normalize_policy.cpp reconcile_header.cpp render_policy.cpp resolve_ledger.cpp resolve_snapshot.cpp server_main.cpp
TARGET  = log_ship

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
