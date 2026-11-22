CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = address_validate.cpp annotate_window.cpp app_db.cpp audit_checkpoint.cpp format_batch.cpp httplib_impl.cpp publish_record.cpp server_main.cpp summarize_label.cpp validate_report.cpp
TARGET  = address_validate

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
