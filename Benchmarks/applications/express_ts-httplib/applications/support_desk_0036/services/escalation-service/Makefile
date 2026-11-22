CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp collect_checkpoint.cpp collect_policy.cpp enrich_batch.cpp escalation_raise.cpp httplib_impl.cpp publish_batch.cpp resolve_header.cpp server_main.cpp validate_manifest.cpp
TARGET  = escalation_raise

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
