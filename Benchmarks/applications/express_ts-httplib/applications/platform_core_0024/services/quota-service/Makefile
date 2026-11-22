CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp build_policy.cpp collect_threshold.cpp format_schedule.cpp httplib_impl.cpp load_policy.cpp quota_enforce.cpp reconcile_policy.cpp server_main.cpp validate_quota.cpp
TARGET  = quota_enforce

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
