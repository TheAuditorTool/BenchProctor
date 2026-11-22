CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp enrich_profile.cpp httplib_impl.cpp load_record.cpp reconcile_index.cpp resolve_bundle.cpp rotate_profile.cpp server_main.cpp supplier_feed.cpp validate_receipt.cpp
TARGET  = supplier_feed

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
