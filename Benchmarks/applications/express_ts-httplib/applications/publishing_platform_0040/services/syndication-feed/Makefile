CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = annotate_index.cpp app_db.cpp fetch_summary.cpp format_checkpoint.cpp httplib_impl.cpp prune_syndication.cpp reconcile_window.cpp server_main.cpp summarize_config.cpp syndication_push.cpp
TARGET  = syndication_push

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
