// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unistd.h>
#include <fcntl.h>

typedef struct evp_cipher_st EVP_CIPHER;
typedef struct evp_cipher_ctx_st EVP_CIPHER_CTX;
extern "C" const EVP_CIPHER *EVP_des_ecb(void);
extern "C" const EVP_CIPHER *EVP_rc4(void);
extern "C" const EVP_CIPHER *EVP_aes_128_cbc(void);
extern "C" const EVP_CIPHER *EVP_aes_256_cbc(void);
extern "C" const EVP_CIPHER *EVP_aes_256_gcm(void);
extern "C" EVP_CIPHER_CTX *EVP_CIPHER_CTX_new(void);
extern "C" int EVP_EncryptInit_ex(EVP_CIPHER_CTX *, const EVP_CIPHER *, void *, const unsigned char *, const unsigned char *);
extern "C" int EVP_EncryptUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, const unsigned char *, int);
extern "C" void EVP_CIPHER_CTX_free(EVP_CIPHER_CTX *);
struct ValueSource { virtual std::string get() const = 0; virtual ~ValueSource() = default; };
struct HeldValue : ValueSource { std::string v; explicit HeldValue(const std::string &s) : v(s) {} std::string get() const override { return v; } };

void benchmark_test_00605(int, char **)
{
    std::string user_input;
    if (const char *user_input_cl = std::getenv("CONTENT_LENGTH")) {
        long user_input_n = std::strtol(user_input_cl, nullptr, 10);
        if (user_input_n > 0 && user_input_n < 1048576) {
            user_input.resize((size_t)user_input_n);
            std::cin.read(&user_input[0], user_input_n);
            user_input.resize((size_t)std::cin.gcount());
        }
    }
    HeldValue _held(user_input);
    const ValueSource &_vs = _held;
    std::string data = _vs.get();
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    const char *_kv = std::getenv("APP_ENC_KEY");
    unsigned char _ckey[32] = {0};
    if (_kv) std::strncpy(reinterpret_cast<char *>(_ckey), _kv, sizeof(_ckey) - 1);
    unsigned char _civ[16] = {0};
    int _ivfd = open("/dev/urandom", O_RDONLY);
    if (_ivfd >= 0) { if (read(_ivfd, _civ, sizeof(_civ)) < 0) _civ[0] = 0; close(_ivfd); }
    EVP_EncryptInit_ex(_ctx, EVP_aes_256_gcm(), nullptr, _ckey, _civ);
    unsigned char _cout[512]; int _coutl = 0;
    EVP_EncryptUpdate(_ctx, _cout, &_coutl, reinterpret_cast<const unsigned char *>(data.c_str()), (int)data.size());
    EVP_CIPHER_CTX_free(_ctx);
}
