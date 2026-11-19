// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00645(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    const char *safe = data;
    if (strcmp(data, "/bin/echo") != 0 && strcmp(data, "/bin/cat") != 0) safe = "/bin/echo";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "grep %s /var/log/app.log", safe);
    FILE *_p = popen(_cmd, "r");
    if (_p) pclose(_p);
}
