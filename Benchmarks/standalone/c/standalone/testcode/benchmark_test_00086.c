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

void benchmark_test_00086(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    unsigned char _iv[12];
    RAND_bytes(_iv, sizeof(_iv));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_EncryptInit_ex(_ctx, EVP_aes_256_gcm(), NULL, (const unsigned char *)getenv("DATA_ENC_KEY"), _iv);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)user_input, (int)strlen(user_input));
    EVP_CIPHER_CTX_free(_ctx);
}
