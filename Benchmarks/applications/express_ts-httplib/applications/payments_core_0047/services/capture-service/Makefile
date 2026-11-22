CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp build_dispute.cpp build_payout.cpp build_threshold.cpp capture_settle.cpp fetch_profile.cpp fetch_record.cpp httplib_impl.cpp reconcile_dispute.cpp server_main.cpp
TARGET  = capture_settle

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
