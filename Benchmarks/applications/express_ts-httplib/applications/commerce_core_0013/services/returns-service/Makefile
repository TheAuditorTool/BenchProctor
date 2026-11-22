CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = annotate_order.cpp audit_roster.cpp compact_record.cpp httplib_impl.cpp normalize_receipt.cpp reconcile_policy.cpp render_bundle.cpp return_request.cpp rotate_index.cpp server_main.cpp
TARGET  = return_request

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
