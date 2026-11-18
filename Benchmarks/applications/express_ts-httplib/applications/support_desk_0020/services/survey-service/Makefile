CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp archive_config.cpp archive_snapshot.cpp httplib_impl.cpp load_bundle.cpp render_ticket.cpp server_main.cpp survey_send.cpp validate_bundle.cpp validate_window.cpp
TARGET  = survey_send

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
