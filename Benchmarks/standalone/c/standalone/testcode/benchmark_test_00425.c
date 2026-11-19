// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

void benchmark_test_00425(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    regex_t _re;
    const char *safe = data;
    if (regcomp(&_re, "^(asc|desc|name|created)$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) safe = "asc";
        regfree(&_re);
    }
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "grep %s /var/log/app.log", safe);
    FILE *_p = popen(_cmd, "r");
    if (_p) pclose(_p);
}
