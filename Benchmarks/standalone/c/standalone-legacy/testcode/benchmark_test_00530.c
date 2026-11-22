// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00530(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    const char *arg = data;
    if (strcmp(data, "/bin/echo") != 0 && strcmp(data, "/bin/cat") != 0) arg = "/bin/echo";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "ls %s", arg);
    system(_cmd);
}
