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

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00485(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    const char *data = c_passthrough(user_input);
    regex_t _re;
    const char *arg = data;
    if (regcomp(&_re, "^[a-zA-Z0-9#._-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) arg = "config";
        regfree(&_re);
    }
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT name, email FROM users WHERE name = '%s'", arg);
    char **_rows = NULL;
    int _nrow = 0, _ncol = 0;
    sqlite3_get_table(_db, _sql, &_rows, &_nrow, &_ncol, NULL);
    for (int _r = 1; _r <= _nrow; ++_r) printf("%s\n", _rows[_r * _ncol + 1]);
    sqlite3_free_table(_rows);
    sqlite3_close(_db);
}
