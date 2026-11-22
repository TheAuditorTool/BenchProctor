CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp cart_update.cpp fetch_summary.cpp format_report.cpp httplib_impl.cpp prune_config.cpp publish_policy.cpp rotate_profile.cpp server_main.cpp summarize_checkpoint.cpp validate_fulfillment.cpp
TARGET  = cart_update

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
