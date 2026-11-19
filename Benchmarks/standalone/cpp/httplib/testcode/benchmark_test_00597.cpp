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
struct pg_conn; typedef struct pg_conn PGconn;
struct pg_result; typedef struct pg_result PGresult;
extern "C" PGconn *PQsetdbLogin(const char *, const char *, const char *, const char *, const char *, const char *, const char *);
extern "C" int PQstatus(const PGconn *);
extern "C" void PQfinish(PGconn *);
extern "C" PGresult *PQexec(PGconn *, const char *);
extern "C" PGresult *PQexecParams(PGconn *, const char *, int, const unsigned int *, const char *const *, const int *, const int *, int);
extern "C" void PQclear(PGresult *);

void benchmark_test_00597(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("X-Custom-Header");
    std::string data = !user_input.empty() ? user_input : std::string();
    PGconn *_pgc = PQsetdbLogin("db.internal", "5432", nullptr, nullptr, "appdb", "app", "");
    const char *_pgvals[1] = { data.c_str() };
    PGresult *_pgr = PQexecParams(_pgc, "SELECT * FROM users WHERE name = $1", 1, nullptr, _pgvals, nullptr, nullptr, 0);
    PQclear(_pgr);
    PQfinish(_pgc);
    res.set_content("ok", "text/plain");
}
