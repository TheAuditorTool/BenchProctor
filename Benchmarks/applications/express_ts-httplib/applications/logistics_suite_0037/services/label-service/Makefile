CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp archive_threshold.cpp build_header.cpp httplib_impl.cpp label_create.cpp publish_receipt.cpp reconcile_checkpoint.cpp resolve_summary.cpp server_main.cpp validate_profile.cpp verify_profile.cpp
TARGET  = label_create

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
