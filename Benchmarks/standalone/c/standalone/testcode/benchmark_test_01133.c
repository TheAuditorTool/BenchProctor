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

void benchmark_test_01133(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    regex_t _re;
    const char *safe = user_input;
    if (regcomp(&_re, "^(asc|desc|name|created)$", REG_EXTENDED) == 0) {
        if (regexec(&_re, user_input, 0, NULL, 0) != 0) safe = "asc";
        regfree(&_re);
    }
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT * FROM users WHERE name = '%s'", safe);
    sqlite3_exec(_db, _sql, NULL, NULL, NULL);
}
