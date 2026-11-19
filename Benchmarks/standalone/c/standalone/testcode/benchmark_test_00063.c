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

void benchmark_test_00063(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/tmp/data", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    regex_t _re;
    const char *safe = user_input;
    if (regcomp(&_re, "^[a-zA-Z0-9#._-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, user_input, 0, NULL, 0) != 0) safe = "config";
        regfree(&_re);
    }
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT * FROM users WHERE name = '%s'", safe);
    sqlite3_exec(_db, _sql, NULL, NULL, NULL);
}
