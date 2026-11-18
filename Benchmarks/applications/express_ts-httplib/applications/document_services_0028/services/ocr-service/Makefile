CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = annotate_schedule.cpp app_db.cpp compact_header.cpp httplib_impl.cpp normalize_config.cpp ocr_extract.cpp publish_checkpoint.cpp render_attachment.cpp render_conversion.cpp server_main.cpp
TARGET  = ocr_extract

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
