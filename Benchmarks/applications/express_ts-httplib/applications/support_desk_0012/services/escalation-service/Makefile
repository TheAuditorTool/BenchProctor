CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp audit_escalation.cpp audit_header.cpp build_header.cpp escalation_raise.cpp httplib_impl.cpp load_threshold.cpp merge_ticket.cpp server_main.cpp validate_checkpoint.cpp
TARGET  = escalation_raise

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
