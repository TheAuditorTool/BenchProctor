// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/sha.h>

void benchmark_test_00568(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    unsigned char _digest[64];
    SHA512((const unsigned char *)data, strlen(data), _digest);
}
