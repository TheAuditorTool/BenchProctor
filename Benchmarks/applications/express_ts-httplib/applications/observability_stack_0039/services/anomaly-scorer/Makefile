CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -lsqlite3 -pthread
SOURCES = anomaly_score.cpp app_db.cpp enrich_metric.cpp format_report.cpp httplib_impl.cpp load_index.cpp render_schedule.cpp rotate_digest.cpp rotate_trace.cpp server_main.cpp verify_report.cpp
TARGET  = anomaly_score

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
