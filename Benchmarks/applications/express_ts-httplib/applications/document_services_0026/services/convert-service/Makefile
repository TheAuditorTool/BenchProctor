CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp archive_bundle.cpp build_manifest.cpp collect_snapshot.cpp compact_roster.cpp convert_job.cpp httplib_impl.cpp render_conversion.cpp render_snapshot.cpp server_main.cpp
TARGET  = convert_job

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
