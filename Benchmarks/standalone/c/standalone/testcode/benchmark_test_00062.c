// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

void benchmark_test_00062(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT * FROM users WHERE name = '%s'", data);
    sqlite3_exec(_db, _sql, NULL, NULL, NULL);
}
