CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = annotate_snapshot.cpp app_db.cpp collect_label.cpp compact_carrier.cpp format_receipt.cpp httplib_impl.cpp load_profile.cpp merge_window.cpp render_checkpoint.cpp server_main.cpp tracking_poll.cpp
TARGET  = tracking_poll

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
