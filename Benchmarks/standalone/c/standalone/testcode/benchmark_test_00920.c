// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

void benchmark_test_00920(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    long _clen = 0;
    const char *_cl = getenv("CONTENT_LENGTH");
    if (_cl != NULL) _clen = strtol(_cl, NULL, 10);
    if (_clen > 0) {
        size_t _rn = (size_t)_clen < sizeof(user_input_buf) - 1 ? (size_t)_clen : sizeof(user_input_buf) - 1;
        size_t _got = fread(user_input_buf, 1, _rn, stdin);
        user_input_buf[_got] = '\0';
    }
    const char *user_input = user_input_buf;
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT * FROM users WHERE name = '%s'", data);
    sqlite3_exec(_db, _sql, NULL, NULL, NULL);
}
