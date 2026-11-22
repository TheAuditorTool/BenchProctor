// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <openssl/evp.h>

void benchmark_test_00176(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    const char *_kv = getenv("DATA_ENC_KEY");
    if (_kv == NULL) return;
    unsigned char _key[32];
    EVP_Digest(_kv, strlen(_kv), _key, NULL, EVP_sha256(), NULL);
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[528];
    int _ctl = 0;
    EVP_EncryptInit_ex2(_ctx, EVP_aes_256_ecb(), _key, NULL, NULL);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strnlen(data, 512));
    EVP_CIPHER_CTX_free(_ctx);
}
