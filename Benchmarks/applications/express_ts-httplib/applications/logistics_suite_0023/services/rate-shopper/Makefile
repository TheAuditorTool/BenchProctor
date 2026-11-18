CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -pthread
SOURCES = archive_config.cpp archive_snapshot.cpp build_snapshot.cpp collect_label.cpp enrich_carrier.cpp httplib_impl.cpp load_header.cpp prune_shipment.cpp rate_shop.cpp server_main.cpp
TARGET  = rate_shop

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
