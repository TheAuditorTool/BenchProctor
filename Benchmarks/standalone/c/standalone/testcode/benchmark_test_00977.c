// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00977(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", data);
    remove(_path);
}
