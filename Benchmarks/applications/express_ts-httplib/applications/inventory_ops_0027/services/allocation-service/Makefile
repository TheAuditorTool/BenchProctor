CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = allocation_solve.cpp app_db.cpp audit_supplier.cpp httplib_impl.cpp merge_threshold.cpp prune_allocation.cpp reconcile_config.cpp reconcile_digest.cpp server_main.cpp summarize_allocation.cpp validate_schedule.cpp
TARGET  = allocation_solve

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
