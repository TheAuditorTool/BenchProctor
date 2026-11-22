CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp build_window.cpp httplib_impl.cpp load_bundle.cpp merge_profile.cpp order_lookup.cpp prune_bundle.cpp publish_promotion.cpp render_summary.cpp resolve_window.cpp server_main.cpp
TARGET  = order_lookup

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
