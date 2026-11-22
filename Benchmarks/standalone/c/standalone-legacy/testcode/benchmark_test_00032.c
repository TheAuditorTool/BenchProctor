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
#include <openssl/hmac.h>

void benchmark_test_00032(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    long _clen = 0;
    const char *_cl = getenv("CONTENT_LENGTH");
    if (_cl != NULL) _clen = strtol(_cl, NULL, 10);
    if (_clen > 0) {
        size_t _rn = (size_t)_clen < sizeof(user_input_buf) - 1 ? (size_t)_clen : sizeof(user_input_buf) - 1;
        size_t _got = fread(user_input_buf, 1, _rn, stdin);
        user_input_buf[_got] = '\0';
    }
    const char *user_input = user_input_buf;
    const char *_kv = getenv("DATA_ENC_KEY");
    if (_kv == NULL) return;
    unsigned char _salt[16], _key[32];
    if (RAND_bytes(_salt, sizeof(_salt)) != 1) return;
    HMAC(EVP_sha256(), _kv, (int)strlen(_kv), _salt, sizeof(_salt), _key, NULL);
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_CipherInit_ex(_ctx, EVP_rc4(), NULL, _key, NULL, 1);
    EVP_CipherUpdate(_ctx, _ct, &_ctl, (const unsigned char *)user_input, (int)strnlen(user_input, sizeof(_ct)));
    EVP_CIPHER_CTX_free(_ctx);
}
