CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp archive_signature.cpp audit_summary.cpp build_roster.cpp build_threshold.cpp convert_job.cpp httplib_impl.cpp reconcile_window.cpp render_conversion.cpp resolve_redaction.cpp server_main.cpp
TARGET  = convert_job

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
