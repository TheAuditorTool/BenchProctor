// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

struct c_ctx { const char *captured; };
static const char *c_capture(const struct c_ctx *c) { const char *_s = c->captured; while (*_s == ' ') _s++; return _s; }

void benchmark_test_00136(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    sqlite3_stmt *_stmt = NULL;
    sqlite3_prepare_v2(_db, "SELECT name, email FROM users WHERE name = ?1", -1, &_stmt, NULL);
    sqlite3_bind_text(_stmt, 1, data, -1, SQLITE_TRANSIENT);
    while (sqlite3_step(_stmt) == SQLITE_ROW) printf("%s\n", (const char *)sqlite3_column_text(_stmt, 1));
    sqlite3_finalize(_stmt);
    sqlite3_close(_db);
}
