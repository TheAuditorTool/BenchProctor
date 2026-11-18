// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unordered_map>
#include <cctype>

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
extern "C" int PQresultStatus(const PGresult *);
extern "C" char *PQgetvalue(const PGresult *, int, int);

void record_decision(const httplib::Request &req, httplib::Response &res)
{
    std::string excerpt;
    {
        const std::string &_body = req.body;
        std::string::size_type _k = _body.find("\"risk_payload\"");
        std::string::size_type _c = _k == std::string::npos ? _k : _body.find(':', _k);
        std::string::size_type _s = _c == std::string::npos ? _c : _body.find('"', _c);
        if (_s != std::string::npos) {
            std::string::size_type _e = _body.find('"', ++_s);
            if (_e != std::string::npos) excerpt = _body.substr(_s, _e - _s);
        }
    }
    PGconn *_pgc = PQsetdbLogin(nullptr, nullptr, nullptr, nullptr, "postgres://app:app@db:5432/app", nullptr, nullptr);
    std::string _pgq = std::string("SELECT * FROM users WHERE name = '") + excerpt + "'";
    PGresult *_pgr = PQexec(_pgc, _pgq.c_str());
    PQclear(_pgr);
    PQfinish(_pgc);
    res.set_content("ok", "text/plain");
}
