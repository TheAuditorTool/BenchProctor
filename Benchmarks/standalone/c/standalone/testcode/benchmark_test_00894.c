// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00894(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", data);
    FILE *_f = fopen(_path, "r");
    if (_f) fclose(_f);
}
