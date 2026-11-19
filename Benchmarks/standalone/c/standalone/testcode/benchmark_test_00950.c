// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>
#include <regex.h>

void benchmark_test_00950(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    regex_t _re;
    const char *safe = data;
    if (regcomp(&_re, "^(asc|desc|name|created)$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) safe = "asc";
        regfree(&_re);
    }
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT * FROM users WHERE name = '%s'", safe);
    sqlite3_exec(_db, _sql, NULL, NULL, NULL);
}
