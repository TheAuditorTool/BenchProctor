// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#if __has_include(<rabbitmq-c/amqp.h>)
#include <rabbitmq-c/amqp.h>
#include <rabbitmq-c/tcp_socket.h>
#else
#include <amqp.h>
#include <amqp_tcp_socket.h>
#endif
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
struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);

void benchmark_test_00529(const httplib::Request &, httplib::Response &res)
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
    std::string _doc = std::string("{\"field\":\"") + user_input + "\"}";
    std::string::size_type _fs = _doc.find("\"field\":\"") + 9;
    std::string::size_type _fe = _doc.find('"', _fs);
    std::string data = _doc.substr(_fs, _fe - _fs);
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT * FROM users WHERE name = '") + data + "'";
    sqlite3_exec(_db, _sqlq.c_str(), nullptr, nullptr, nullptr);
    res.set_content("ok", "text/plain");
}
