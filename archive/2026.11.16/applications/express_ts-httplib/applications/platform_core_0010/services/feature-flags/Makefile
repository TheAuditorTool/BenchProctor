CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp audit_quota.cpp flag_evaluate.cpp httplib_impl.cpp merge_window.cpp normalize_receipt.cpp publish_config.cpp render_snapshot.cpp resolve_ledger.cpp server_main.cpp
TARGET  = flag_evaluate

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
