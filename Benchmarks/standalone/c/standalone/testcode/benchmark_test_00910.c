// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

void benchmark_test_00910(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    unsigned char _iv[8];
    RAND_bytes(_iv, sizeof(_iv));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_EncryptInit_ex(_ctx, EVP_des_ede3_cbc(), NULL, (const unsigned char *)getenv("DATA_ENC_KEY"), _iv);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strlen(data));
    EVP_CIPHER_CTX_free(_ctx);
}
