// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

void benchmark_test_00540(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT name, email FROM users WHERE name = '%s'", data);
    char **_rows = NULL;
    int _nrow = 0, _ncol = 0;
    sqlite3_get_table(_db, _sql, &_rows, &_nrow, &_ncol, NULL);
    for (int _r = 1; _r <= _nrow; ++_r) printf("%s\n", _rows[_r * _ncol + 1]);
    sqlite3_free_table(_rows);
    sqlite3_close(_db);
}
