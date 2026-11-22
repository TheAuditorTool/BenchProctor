CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp build_checkpoint.cpp collect_bundle.cpp connector_invoke.cpp httplib_impl.cpp normalize_record.cpp prune_webhook.cpp publish_config.cpp server_main.cpp summarize_policy.cpp summarize_record.cpp
TARGET  = connector_invoke

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
