CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = annotate_report.cpp app_db.cpp compact_quota.cpp export_manifest.cpp fetch_ledger.cpp httplib_impl.cpp reconcile_checkpoint.cpp render_policy.cpp server_main.cpp tenant_provision.cpp validate_tenant.cpp
TARGET  = tenant_provision

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
