CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = annotate_policy.cpp app_db.cpp build_ledger.cpp build_summary.cpp httplib_impl.cpp payment_capture.cpp render_batch.cpp render_invoice.cpp render_snapshot.cpp server_main.cpp
TARGET  = payment_capture

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
