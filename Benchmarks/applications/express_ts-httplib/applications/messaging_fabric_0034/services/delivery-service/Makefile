CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp archive_checkpoint.cpp delivery_dispatch.cpp httplib_impl.cpp normalize_config.cpp normalize_receipt.cpp normalize_schedule.cpp publish_summary.cpp resolve_checkpoint.cpp server_main.cpp
TARGET  = delivery_dispatch

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
