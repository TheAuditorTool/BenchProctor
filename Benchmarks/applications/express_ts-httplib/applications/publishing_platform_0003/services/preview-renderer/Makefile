CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp audit_batch.cpp compact_revision.cpp httplib_impl.cpp normalize_bundle.cpp preview_render.cpp publish_header.cpp publish_schedule.cpp server_main.cpp summarize_syndication.cpp validate_snapshot.cpp
TARGET  = preview_render

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
