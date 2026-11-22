// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00179(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "%s", user_input);
    execl("/bin/sh", "sh", "-c", _cmd, (char *)NULL);
}
