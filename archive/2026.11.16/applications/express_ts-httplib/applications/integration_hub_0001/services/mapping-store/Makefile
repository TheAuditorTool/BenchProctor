CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = audit_report.cpp collect_bundle.cpp enrich_snapshot.cpp export_snapshot.cpp field_mapping.cpp format_partner.cpp httplib_impl.cpp publish_batch.cpp rotate_digest.cpp server_main.cpp
TARGET  = field_mapping

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
