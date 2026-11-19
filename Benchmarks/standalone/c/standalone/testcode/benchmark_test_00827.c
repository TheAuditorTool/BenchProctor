// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/sha.h>

struct c_payload { const char *value; };

void benchmark_test_00827(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    unsigned char _digest[32];
    SHA256((const unsigned char *)data, strlen(data), _digest);
}
