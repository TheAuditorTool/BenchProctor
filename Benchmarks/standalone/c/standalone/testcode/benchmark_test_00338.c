// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <sqlite3.h>

void benchmark_test_00338(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    sqlite3 *_db = NULL;
    sqlite3_open("/var/app/app.db", &_db);
    char _sql[512];
    snprintf(_sql, sizeof(_sql), "SELECT * FROM users WHERE name = '%s'", data);
    sqlite3_exec(_db, _sql, NULL, NULL, NULL);
}
