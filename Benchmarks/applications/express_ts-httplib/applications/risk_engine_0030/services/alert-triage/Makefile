CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -pthread
SOURCES = alert_triage.cpp archive_rule.cpp archive_schedule.cpp build_decision.cpp compact_roster.cpp enrich_schedule.cpp httplib_impl.cpp reconcile_batch.cpp server_main.cpp
TARGET  = alert_triage

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
