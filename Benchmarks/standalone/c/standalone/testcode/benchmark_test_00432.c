// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/rand.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00432(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = c_passthrough(user_input);
    unsigned char _rnd[16];
    if (RAND_bytes(_rnd, sizeof(_rnd)) != 1) return;
    char _hex[33];
    for (int _i = 0; _i < 16; _i++) snprintf(_hex + 2 * _i, 3, "%02x", _rnd[_i]);
    printf("token for %s: %s\n", data, _hex);
}
