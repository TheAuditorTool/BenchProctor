CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp customs_declare.cpp export_index.cpp export_profile.cpp httplib_impl.cpp merge_label.cpp reconcile_profile.cpp server_main.cpp verify_manifest.cpp verify_window.cpp
TARGET  = customs_declare

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
