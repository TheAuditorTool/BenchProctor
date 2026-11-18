// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
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
struct pg_conn; typedef struct pg_conn PGconn;
struct pg_result; typedef struct pg_result PGresult;
extern "C" PGconn *PQsetdbLogin(const char *, const char *, const char *, const char *, const char *, const char *, const char *);
extern "C" int PQstatus(const PGconn *);
extern "C" void PQfinish(PGconn *);
extern "C" PGresult *PQexec(PGconn *, const char *);
extern "C" PGresult *PQexecParams(PGconn *, const char *, int, const unsigned int *, const char *const *, const int *, const int *, int);
extern "C" void PQclear(PGresult *);

void benchmark_test_00283(const httplib::Request &, httplib::Response &res)
{
    const char *user_input_env = std::getenv("APP_INPUT");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    data.reserve(user_input.size());
    for (char _c : user_input) data.push_back(_c);
    PGconn *_pgc = PQsetdbLogin("db.internal", "5432", nullptr, nullptr, "appdb", "app", "");
    const char *_pgvals[1] = { data.c_str() };
    PGresult *_pgr = PQexecParams(_pgc, "SELECT * FROM users WHERE name = $1", 1, nullptr, _pgvals, nullptr, nullptr, 0);
    PQclear(_pgr);
    PQfinish(_pgc);
    res.set_content("ok", "text/plain");
}
