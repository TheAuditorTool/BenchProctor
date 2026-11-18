CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp comment_post.cpp export_policy.cpp fetch_comment.cpp httplib_impl.cpp load_digest.cpp load_snapshot.cpp reconcile_snapshot.cpp server_main.cpp validate_config.cpp
TARGET  = comment_post

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
