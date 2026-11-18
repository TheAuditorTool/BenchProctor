CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -pthread
SOURCES = archive_checkpoint.cpp collect_receipt.cpp httplib_impl.cpp load_digest.cpp load_record.cpp mfa_verify.cpp resolve_bundle.cpp server_main.cpp verify_config.cpp
TARGET  = mfa_verify

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
