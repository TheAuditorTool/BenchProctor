CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp compact_shipment.cpp enrich_header.cpp enrich_summary.cpp httplib_impl.cpp prune_label.cpp reconcile_config.cpp server_main.cpp tracking_poll.cpp validate_profile.cpp
TARGET  = tracking_poll

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
