CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = annotate_index.cpp app_db.cpp export_policy.cpp format_window.cpp httplib_impl.cpp load_batch.cpp merge_profile.cpp payment_authorize.cpp rotate_payout.cpp server_main.cpp
TARGET  = payment_authorize

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
