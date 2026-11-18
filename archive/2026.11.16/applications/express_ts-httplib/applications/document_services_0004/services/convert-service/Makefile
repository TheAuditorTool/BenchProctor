CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp convert_job.cpp format_summary.cpp httplib_impl.cpp merge_digest.cpp publish_manifest.cpp publish_receipt.cpp reconcile_profile.cpp server_main.cpp validate_manifest.cpp
TARGET  = convert_job

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
