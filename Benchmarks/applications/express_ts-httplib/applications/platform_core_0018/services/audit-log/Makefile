CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -lrabbitmq -lsqlite3 -pthread
SOURCES = app_db.cpp archive_checkpoint.cpp audit_append.cpp fetch_roster.cpp httplib_impl.cpp normalize_flag.cpp render_secret.cpp server_main.cpp validate_policy.cpp validate_tenant.cpp
TARGET  = audit_append

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
