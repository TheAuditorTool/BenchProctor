CC      = c++
CFLAGS  = -std=c++17 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = annotate_summary.cpp app_db.cpp audit_manifest.cpp format_revision.cpp httplib_impl.cpp preview_render.cpp prune_article.cpp prune_threshold.cpp publish_window.cpp server_main.cpp
TARGET  = preview_render

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
