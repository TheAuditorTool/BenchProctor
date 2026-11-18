CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lsqlite3 -pthread
SOURCES = app_db.cpp audit_schedule.cpp directory_sync.cpp httplib_impl.cpp normalize_session.cpp reconcile_batch.cpp server_main.cpp validate_record.cpp verify_checkpoint.cpp verify_schedule.cpp
TARGET  = directory_sync

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
