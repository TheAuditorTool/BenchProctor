// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <unordered_map>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
}
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
extern "C" int RAND_bytes(unsigned char *buf, int num);
struct env_md_st; typedef struct env_md_st EVP_MD;
extern "C" const EVP_MD *EVP_sha256(void);
extern "C" unsigned char *HMAC(const EVP_MD *, const void *, int, const unsigned char *, size_t, unsigned char *, unsigned int *);
extern "C" int EVP_CipherInit_ex(EVP_CIPHER_CTX *, const EVP_CIPHER *, void *, const unsigned char *, const unsigned char *, int);
extern "C" int EVP_CipherUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, const unsigned char *, int);

void benchmark_test_00010(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.body;
    std::string data;
    std::string::size_type _w = 0;
    while (_w < user_input.size()) { data.push_back(user_input[_w]); ++_w; }
    const char *_kv = std::getenv("APP_ENC_KEY");
    unsigned char _ckey[32] = {0};
    if (_kv) std::strncpy(reinterpret_cast<char *>(_ckey), _kv, sizeof(_ckey) - 1);
    int _clen = data.size() > 512 ? 512 : static_cast<int>(data.size());
    unsigned char _salt[16], _mkey[32];
    if (RAND_bytes(_salt, sizeof(_salt)) != 1) return;
    HMAC(EVP_sha256(), _ckey, sizeof(_ckey), _salt, sizeof(_salt), _mkey, nullptr);
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    EVP_CipherInit_ex(_ctx, EVP_rc4(), nullptr, _mkey, nullptr, 1);
    unsigned char _cout[512]; int _coutl = 0;
    EVP_CipherUpdate(_ctx, _cout, &_coutl, reinterpret_cast<const unsigned char *>(data.c_str()), _clen);
    EVP_CIPHER_CTX_free(_ctx);
    res.set_content("ok", "text/plain");
}
