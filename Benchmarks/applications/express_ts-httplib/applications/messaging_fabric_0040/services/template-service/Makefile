CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lpq -lsqlite3 -pthread
SOURCES = annotate_window.cpp app_db.cpp collect_summary.cpp httplib_impl.cpp normalize_profile.cpp prune_roster.cpp server_main.cpp template_compose.cpp validate_schedule.cpp verify_delivery.cpp
TARGET  = template_compose

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
