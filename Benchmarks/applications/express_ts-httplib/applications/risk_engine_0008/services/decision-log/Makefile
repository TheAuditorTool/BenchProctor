CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lpq -lsqlite3 -pthread
SOURCES = app_db.cpp audit_threshold.cpp decision_record.cpp httplib_impl.cpp merge_digest.cpp merge_roster.cpp publish_report.cpp render_rule.cpp server_main.cpp verify_profile.cpp
TARGET  = decision_record

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
