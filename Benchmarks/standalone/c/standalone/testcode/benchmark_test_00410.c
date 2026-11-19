// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00410(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "grep %s /var/log/app.log", user_input);
    FILE *_p = popen(_cmd, "r");
    if (_p) pclose(_p);
}
