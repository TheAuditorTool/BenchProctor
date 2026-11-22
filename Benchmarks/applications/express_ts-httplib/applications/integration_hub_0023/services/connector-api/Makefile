CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp connector_invoke.cpp httplib_impl.cpp load_partner.cpp load_summary.cpp merge_receipt.cpp reconcile_snapshot.cpp render_roster.cpp server_main.cpp verify_manifest.cpp verify_threshold.cpp
TARGET  = connector_invoke

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
