CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = activity_stream.cpp annotate_policy.cpp annotate_snapshot.cpp app_db.cpp audit_membership.cpp collect_threshold.cpp httplib_impl.cpp load_index.cpp normalize_record.cpp rotate_profile.cpp server_main.cpp
TARGET  = activity_stream

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
