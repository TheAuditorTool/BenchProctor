CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -lsqlite3 -pthread
SOURCES = annotate_schedule.cpp app_db.cpp compact_cart.cpp compact_roster.cpp fetch_roster.cpp httplib_impl.cpp normalize_fulfillment.cpp order_lookup.cpp prune_receipt.cpp resolve_roster.cpp server_main.cpp
TARGET  = order_lookup

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
