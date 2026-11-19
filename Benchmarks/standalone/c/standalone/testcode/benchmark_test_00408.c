// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00408(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = c_passthrough(user_input);
    const char *safe = data;
    if (strcmp(data, "/bin/echo") != 0 && strcmp(data, "/bin/cat") != 0) safe = "/bin/echo";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "%s", safe);
    execl("/bin/sh", "sh", "-c", _cmd, (char *)NULL);
}
