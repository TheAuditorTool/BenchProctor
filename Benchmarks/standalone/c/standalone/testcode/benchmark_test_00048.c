// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00048(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    const char *data = c_passthrough(user_input);
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    sqlite3_stmt *_stmt = NULL;
    sqlite3_prepare_v2(_db, "SELECT * FROM users WHERE name = ?1", -1, &_stmt, NULL);
    sqlite3_bind_text(_stmt, 1, data, -1, SQLITE_TRANSIENT);
    sqlite3_step(_stmt);
    sqlite3_finalize(_stmt);
    sqlite3_close(_db);
}
