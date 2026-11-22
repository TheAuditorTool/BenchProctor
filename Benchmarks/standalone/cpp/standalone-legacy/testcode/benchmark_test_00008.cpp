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

struct sqlite3; struct sqlite3_stmt;
extern "C" int sqlite3_open(const char *, sqlite3 **);
extern "C" int sqlite3_exec(sqlite3 *, const char *, int (*)(void *, int, char **, char **), void *, char **);
extern "C" int sqlite3_prepare_v2(sqlite3 *, const char *, int, sqlite3_stmt **, const char **);
extern "C" int sqlite3_bind_text(sqlite3_stmt *, int, const char *, int, void (*)(void *));
extern "C" int sqlite3_step(sqlite3_stmt *);
extern "C" int sqlite3_finalize(sqlite3_stmt *);

void benchmark_test_00008(int, char **)
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
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    sqlite3_stmt *_st = nullptr;
    sqlite3_prepare_v2(_db, "SELECT * FROM users WHERE name = ?", -1, &_st, nullptr);
    sqlite3_bind_text(_st, 1, data.c_str(), -1, nullptr);
    sqlite3_step(_st);
    sqlite3_finalize(_st);
}
