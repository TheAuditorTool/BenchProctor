CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp archive_receipt.cpp compact_profile.cpp delivery_dispatch.cpp enrich_delivery.cpp httplib_impl.cpp load_subscription.cpp publish_roster.cpp resolve_window.cpp server_main.cpp
TARGET  = delivery_dispatch

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
