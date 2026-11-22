CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp httplib_impl.cpp normalize_report.cpp publish_threshold.cpp reconcile_threshold.cpp redaction_apply.cpp rotate_bundle.cpp server_main.cpp validate_index.cpp verify_snapshot.cpp
TARGET  = redaction_apply

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
