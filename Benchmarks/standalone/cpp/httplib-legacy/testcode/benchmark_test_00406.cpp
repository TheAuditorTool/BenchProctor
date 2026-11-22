// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <spawn.h>
#include <sys/wait.h>
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

void benchmark_test_00406(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_param_value("id");
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    static const std::regex _re("^[a-zA-Z0-9 _.%\\-]+$");
    std::string arg = std::regex_match(data, _re) ? data : std::string("default");
    const char *_sp_argv[] = { "sh", "-c", arg.c_str(), nullptr };
    char *const _sp_env[] = { nullptr };
    pid_t _pid;
    if (posix_spawn(&_pid, "/bin/sh", nullptr, nullptr, const_cast<char *const *>(_sp_argv), _sp_env) == 0) waitpid(_pid, nullptr, 0);
    res.set_content("ok", "text/plain");
}
