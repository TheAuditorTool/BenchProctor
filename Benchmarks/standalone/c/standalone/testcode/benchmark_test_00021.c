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

void benchmark_test_00021(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    unsigned char _iv[12];
    RAND_bytes(_iv, sizeof(_iv));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_EncryptInit_ex(_ctx, EVP_aes_256_gcm(), NULL, (const unsigned char *)getenv("DATA_ENC_KEY"), _iv);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strlen(data));
    EVP_CIPHER_CTX_free(_ctx);
}
