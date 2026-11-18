CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lhiredis -lsqlite3 -pthread
SOURCES = annotate_digest.cpp app_db.cpp export_digest.cpp fetch_digest.cpp format_comment.cpp httplib_impl.cpp prune_schedule.cpp rotate_digest.cpp server_main.cpp share_grant.cpp
TARGET  = share_grant

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
