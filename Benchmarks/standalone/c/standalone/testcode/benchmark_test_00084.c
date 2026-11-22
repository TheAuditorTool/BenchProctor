// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

void benchmark_test_00084(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    sqlite3_stmt *_stmt = NULL;
    sqlite3_prepare_v2(_db, "SELECT * FROM users WHERE name = ?1", -1, &_stmt, NULL);
    sqlite3_bind_text(_stmt, 1, data, -1, SQLITE_TRANSIENT);
    sqlite3_step(_stmt);
    sqlite3_finalize(_stmt);
    sqlite3_close(_db);
}
