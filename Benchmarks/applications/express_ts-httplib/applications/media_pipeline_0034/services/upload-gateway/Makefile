CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp asset_upload.cpp export_profile.cpp httplib_impl.cpp reconcile_report.cpp render_caption.cpp server_main.cpp summarize_record.cpp validate_checkpoint.cpp validate_schedule.cpp
TARGET  = asset_upload

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
