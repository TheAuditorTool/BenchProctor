CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp audit_header.cpp audit_report.cpp httplib_impl.cpp manifest_build.cpp reconcile_threshold.cpp rotate_config.cpp server_main.cpp verify_checkpoint.cpp verify_manifest.cpp
TARGET  = manifest_build

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
