CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp collect_receipt.cpp enrich_ticket.cpp fetch_manifest.cpp httplib_impl.cpp prune_policy.cpp render_checkpoint.cpp rotate_checkpoint.cpp server_main.cpp ticket_route.cpp verify_roster.cpp
TARGET  = ticket_route

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
