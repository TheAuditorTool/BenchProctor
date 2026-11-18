CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = annotate_schedule.cpp app_db.cpp httplib_impl.cpp load_manifest.cpp normalize_manifest.cpp prune_metric.cpp publish_sample.cpp retention_sweep.cpp rotate_ledger.cpp server_main.cpp
TARGET  = retention_sweep

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
