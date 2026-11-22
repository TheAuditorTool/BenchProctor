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

void benchmark_test_00052(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/etc/app/config", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    const char *_kv = getenv("DATA_ENC_KEY");
    if (_kv == NULL) return;
    unsigned char _key[32];
    EVP_Digest(_kv, strlen(_kv), _key, NULL, EVP_sha256(), NULL);
    unsigned char _iv[12];
    RAND_bytes(_iv, sizeof(_iv));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[528];
    int _ctl = 0;
    EVP_EncryptInit_ex2(_ctx, EVP_aes_256_gcm(), _key, _iv, NULL);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)user_input, (int)strnlen(user_input, 512));
    EVP_CIPHER_CTX_free(_ctx);
}
