CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp compact_receipt.cpp fetch_schedule.cpp httplib_impl.cpp prune_report.cpp resolve_snapshot.cpp rotate_report.cpp server_main.cpp settlement_batch.cpp validate_schedule.cpp
TARGET  = settlement_batch

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
