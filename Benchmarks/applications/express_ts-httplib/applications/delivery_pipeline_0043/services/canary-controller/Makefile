CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp build_receipt.cpp canary_promote.cpp collect_threshold.cpp httplib_impl.cpp prune_window.cpp publish_record.cpp rotate_policy.cpp server_main.cpp verify_report.cpp
TARGET  = canary_promote

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
