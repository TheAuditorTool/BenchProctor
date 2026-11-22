CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -pthread
SOURCES = build_index.cpp enrich_policy.cpp httplib_impl.cpp load_policy.cpp merge_header.cpp normalize_receipt.cpp prune_release.cpp publish_window.cpp rollback_trigger.cpp server_main.cpp
TARGET  = rollback_trigger

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
