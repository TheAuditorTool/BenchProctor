// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00479(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "%s", data);
    execl("/bin/sh", "sh", "-c", _cmd, (char *)NULL);
}
