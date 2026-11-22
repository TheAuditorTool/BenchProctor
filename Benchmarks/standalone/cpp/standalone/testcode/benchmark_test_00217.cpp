// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <regex>
#if __has_include(<rabbitmq-c/amqp.h>)
#include <rabbitmq-c/amqp.h>
#include <rabbitmq-c/tcp_socket.h>
#else
#include <amqp.h>
#include <amqp_tcp_socket.h>
#endif

typedef void CURL;
extern "C" CURL *curl_easy_init(void);
extern "C" int curl_easy_setopt(CURL *, int, ...);
extern "C" int curl_easy_perform(CURL *);
extern "C" void curl_easy_cleanup(CURL *);
enum { CURLOPT_URL = 10002, CURLOPT_SSL_VERIFYPEER = 64, CURLOPT_SSL_VERIFYHOST = 81, CURLOPT_SSL_VERIFYSTATUS = 232, CURLOPT_POSTFIELDS = 10015, CURLOPT_CUSTOMREQUEST = 10036, CURLOPT_WRITEFUNCTION = 20011, CURLOPT_WRITEDATA = 10001 };

void benchmark_test_00217(int, char **)
{
    std::string user_input;
    amqp_connection_state_t _amqp = amqp_new_connection();
    amqp_socket_t *_amqp_sock = amqp_tcp_socket_new(_amqp);
    if (_amqp_sock != nullptr && amqp_socket_open(_amqp_sock, "broker", 5672) == AMQP_STATUS_OK && amqp_login(_amqp, "/", 0, 131072, 0, AMQP_SASL_METHOD_PLAIN, "guest", "guest").reply_type == AMQP_RESPONSE_NORMAL && amqp_channel_open(_amqp, 1) != nullptr) {
        amqp_rpc_reply_t _amqp_get = amqp_basic_get(_amqp, 1, amqp_cstring_bytes("app-events"), 1);
        amqp_message_t _amqp_msg;
        if (_amqp_get.reply_type == AMQP_RESPONSE_NORMAL && _amqp_get.reply.id == AMQP_BASIC_GET_OK_METHOD && amqp_read_message(_amqp, 1, &_amqp_msg, 0).reply_type == AMQP_RESPONSE_NORMAL) {
            user_input.assign(static_cast<const char *>(_amqp_msg.body.bytes), _amqp_msg.body.len);
            amqp_destroy_message(&_amqp_msg);
        }
    }
    amqp_destroy_connection(_amqp);
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    std::string _authority = data;
    std::string::size_type _scheme = _authority.find("://");
    if (_scheme != std::string::npos) _authority = _authority.substr(_scheme + 3);
    else if (_authority.rfind("//", 0) == 0) _authority = _authority.substr(2);
    _authority = _authority.substr(0, _authority.find_first_of("/?#"));
    std::string::size_type _userinfo = _authority.rfind('@');
    if (_userinfo != std::string::npos) _authority = _authority.substr(_userinfo + 1);
    _authority = _authority.substr(0, _authority.find(':'));
    static const std::regex _hw("^(api\\.internal\\.example\\.com|cdn\\.internal\\.example\\.com)$");
    if (!std::regex_match(_authority, _hw)) return;
    std::string arg = data;
    std::string _hurl = arg;
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, _hurl.c_str());
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
