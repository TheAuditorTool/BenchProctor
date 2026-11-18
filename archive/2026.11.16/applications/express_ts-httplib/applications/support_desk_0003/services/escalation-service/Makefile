CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp compact_macro.cpp compact_report.cpp escalation_raise.cpp fetch_roster.cpp format_summary.cpp httplib_impl.cpp normalize_record.cpp prune_threshold.cpp server_main.cpp summarize_checkpoint.cpp
TARGET  = escalation_raise

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
