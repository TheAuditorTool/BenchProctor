CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp audit_bundle.cpp compact_digest.cpp compact_dunning.cpp export_header.cpp export_summary.cpp format_statement.cpp httplib_impl.cpp refund_issue.cpp server_main.cpp
TARGET  = refund_issue

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
