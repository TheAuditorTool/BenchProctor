CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp audit_batch.cpp audit_record.cpp build_signature.cpp document_upload.cpp enrich_manifest.cpp httplib_impl.cpp load_receipt.cpp reconcile_threshold.cpp server_main.cpp
TARGET  = document_upload

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
