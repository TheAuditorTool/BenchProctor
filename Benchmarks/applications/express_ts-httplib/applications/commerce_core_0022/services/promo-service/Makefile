CC      = c++
CFLAGS  = -std=c++14 -O2 -Wall -pthread
LDLIBS  = -lsqlite3 -pthread
SOURCES = app_db.cpp archive_policy.cpp collect_threshold.cpp httplib_impl.cpp merge_manifest.cpp merge_profile.cpp promo_apply.cpp prune_promotion.cpp resolve_cart.cpp server_main.cpp
TARGET  = promo_apply

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $@ $(SOURCES) $(LDLIBS)

clean:
	rm -f $(TARGET)

.PHONY: all clean
