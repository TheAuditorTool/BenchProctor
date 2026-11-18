// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
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

void benchmark_test_00092(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Cookie");
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    EVP_CIPHER_CTX *_ctx = EVP_CIPHER_CTX_new();
    unsigned char _ckey[32] = {0};
    EVP_EncryptInit_ex(_ctx, EVP_des_ecb(), nullptr, _ckey, nullptr);
    unsigned char _cout[512]; int _coutl = 0;
    EVP_EncryptUpdate(_ctx, _cout, &_coutl, reinterpret_cast<const unsigned char *>(data.c_str()), (int)data.size());
    EVP_CIPHER_CTX_free(_ctx);
    res.set_content("ok", "text/plain");
}
