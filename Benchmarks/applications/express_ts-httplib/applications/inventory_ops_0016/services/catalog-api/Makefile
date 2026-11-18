CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = collect_schedule.cpp export_digest.cpp fetch_supplier.cpp format_digest.cpp httplib_impl.cpp rotate_threshold.cpp server_main.cpp sku_lookup.cpp summarize_reservation.cpp
TARGET  = sku_lookup

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
