CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = anomaly_score.cpp audit_config.cpp build_policy.cpp compact_digest.cpp fetch_trace.cpp format_digest.cpp httplib_impl.cpp reconcile_bundle.cpp reconcile_roster.cpp server_main.cpp
TARGET  = anomaly_score

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
