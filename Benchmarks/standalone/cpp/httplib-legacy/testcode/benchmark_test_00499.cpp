// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <unistd.h>
#include <regex>
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
extern "C" int sqlite3_get_table(sqlite3 *, const char *, char ***, int *, int *, char **); extern "C" void sqlite3_free_table(char **);

void benchmark_test_00499(const httplib::Request &, httplib::Response &res)
{
    std::string user_input;
    if (FILE *_fp = std::fopen("/etc/app/config", "r")) {
        char _b[256];
        if (std::fgets(_b, sizeof(_b), _fp)) {
            _b[std::strcspn(_b, "\n")] = 0;
            user_input = _b;
        }
        std::fclose(_fp);
    }
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    static const std::regex _re("^[a-zA-Z0-9_.#\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    sqlite3 *_db = nullptr;
    sqlite3_open("app.db", &_db);
    std::string _sqlq = std::string("SELECT name, email FROM users WHERE name = '") + arg + "'";
    char **_rows = nullptr;
    int _nrow = 0, _ncol = 0;
    sqlite3_get_table(_db, _sqlq.c_str(), &_rows, &_nrow, &_ncol, nullptr);
    for (int _r = 1; _r <= _nrow; ++_r) std::cout << _rows[_r * _ncol + 1] << std::endl;
    sqlite3_free_table(_rows);
    res.set_content("ok", "text/plain");
}
