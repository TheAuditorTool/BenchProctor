// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00362(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    const char *arg = data;
    if (strcmp(data, "/bin/echo") != 0 && strcmp(data, "/bin/cat") != 0) arg = "/bin/echo";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "%s", arg);
    execl("/bin/sh", "sh", "-c", _cmd, (char *)NULL);
}
