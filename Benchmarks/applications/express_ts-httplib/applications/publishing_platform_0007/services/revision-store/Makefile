CC      = c++
CFLAGS  = -std=c++20 -O2 -Wall -pthread
LDLIBS  = -lcurl -pthread
SOURCES = archive_record.cpp build_index.cpp build_ledger.cpp build_window.cpp httplib_impl.cpp publish_article.cpp revision_save.cpp server_main.cpp validate_taxonomy.cpp
TARGET  = revision_save

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
