// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/md5.h>

struct c_payload { const char *value; };

void benchmark_test_00074(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    unsigned char _digest[16];
    MD5((const unsigned char *)data, strlen(data), _digest);
}
