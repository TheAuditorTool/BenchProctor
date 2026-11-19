// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00065(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char _resolved[1024];
    char _joined[1024];
    snprintf(_joined, sizeof(_joined), "/var/app/data/%s", user_input);
    if (realpath(_joined, _resolved) == NULL) return;
    if (strncmp(_resolved, "/var/app/data/", 14) != 0) return;
    const char *safe = _resolved;
    remove(safe);
}
