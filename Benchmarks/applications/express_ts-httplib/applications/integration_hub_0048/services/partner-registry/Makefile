CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp archive_header.cpp audit_window.cpp enrich_config.cpp httplib_impl.cpp normalize_index.cpp partner_register.cpp publish_roster.cpp server_main.cpp verify_connector.cpp
TARGET  = partner_register

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
