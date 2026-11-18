CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -pthread
SOURCES = annotate_caption.cpp build_roster.cpp fetch_ledger.cpp httplib_impl.cpp load_threshold.cpp render_schedule.cpp rotate_index.cpp server_main.cpp thumbnail_render.cpp
TARGET  = thumbnail_render

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
