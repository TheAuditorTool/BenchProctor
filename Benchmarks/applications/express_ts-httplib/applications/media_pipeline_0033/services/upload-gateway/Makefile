CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = asset_upload.cpp audit_config.cpp collect_bundle.cpp enrich_stream.cpp export_window.cpp httplib_impl.cpp merge_summary.cpp prune_receipt.cpp render_receipt.cpp server_main.cpp
TARGET  = asset_upload

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
