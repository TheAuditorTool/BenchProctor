// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00446(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    char _resolved[1024];
    char _joined[1024];
    snprintf(_joined, sizeof(_joined), "/var/app/data/%s", data);
    if (realpath(_joined, _resolved) == NULL) return;
    if (strncmp(_resolved, "/var/app/data/", 14) != 0) return;
    const char *safe = _resolved;
    remove(safe);
}
