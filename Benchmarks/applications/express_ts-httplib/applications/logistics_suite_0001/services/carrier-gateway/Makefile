CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp audit_shipment.cpp carrier_dispatch.cpp collect_label.cpp enrich_roster.cpp fetch_profile.cpp httplib_impl.cpp rotate_label.cpp server_main.cpp validate_policy.cpp verify_carrier.cpp
TARGET  = carrier_dispatch

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
