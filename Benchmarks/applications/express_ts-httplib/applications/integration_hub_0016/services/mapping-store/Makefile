CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lhiredis -lsqlite3 -pthread
SOURCES = app_db.cpp export_record.cpp field_mapping.cpp format_mapping.cpp httplib_impl.cpp merge_manifest.cpp prune_index.cpp publish_connector.cpp server_main.cpp validate_snapshot.cpp
TARGET  = field_mapping

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
