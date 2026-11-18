CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -lsqlite3 -pthread
SOURCES = alert_route.cpp app_db.cpp audit_digest.cpp build_snapshot.cpp compact_receipt.cpp export_schedule.cpp httplib_impl.cpp reconcile_sample.cpp rotate_checkpoint.cpp server_main.cpp
TARGET  = alert_route

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
