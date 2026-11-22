// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/md5.h>

void benchmark_test_00279(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    unsigned char _digest[16];
    MD5((const unsigned char *)user_input, strlen(user_input), _digest);
}
