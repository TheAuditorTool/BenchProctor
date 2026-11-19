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

struct c_ctx { const char *captured; };
static const char *c_capture(const struct c_ctx *c) { const char *_s = c->captured; while (*_s == ' ') _s++; return _s; }

void benchmark_test_00791(int argc, char **argv)
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
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    unsigned char _iv[12];
    RAND_bytes(_iv, sizeof(_iv));
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ct[512];
    int _ctl = 0;
    EVP_EncryptInit_ex(_ctx, EVP_aes_256_gcm(), NULL, (const unsigned char *)getenv("DATA_ENC_KEY"), _iv);
    EVP_EncryptUpdate(_ctx, _ct, &_ctl, (const unsigned char *)data, (int)strlen(data));
    EVP_CIPHER_CTX_free(_ctx);
}
