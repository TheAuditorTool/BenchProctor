CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp audit_threshold.cpp export_record.cpp export_window.cpp httplib_impl.cpp merge_window.cpp normalize_profile.cpp resolve_report.cpp server_main.cpp tenant_provision.cpp verify_checkpoint.cpp
TARGET  = tenant_provision

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
