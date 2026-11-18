CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lcurl -lsqlite3 -pthread
SOURCES = app_db.cpp article_draft.cpp audit_checkpoint.cpp audit_header.cpp fetch_header.cpp httplib_impl.cpp render_article.cpp resolve_batch.cpp rotate_ledger.cpp server_main.cpp verify_digest.cpp
TARGET  = article_draft

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
