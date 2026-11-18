# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "resolv"
require "ipaddr"
require "socket"

class BenchmarkTest00003 < Sinatra::Base
  before do
    halt 413 if request.content_length.to_i > 1_000_000
  end
  after do
    headers["X-Content-Type-Options"] = "nosniff"
  end

  error StandardError do
    content_type :json
    status 500
    JSON.generate({ error: "internal" })
  end
  post "/benchmark_test_00003" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    _host = (URI.parse(data).host rescue nil)
    _ip = _host ? (Resolv.getaddress(_host) rescue nil) : nil
    if _ip.nil? || "10.0.0.0/8 127.0.0.0/8 169.254.0.0/16 172.16.0.0/12 192.168.0.0/16 0.0.0.0/8 ::1/128 fc00::/7 fe80::/10".split.any? { |c| IPAddr.new(c).include?(_ip) rescue false }
      halt 403, JSON.generate({ error: "private range blocked" })
      return
    end
    target_url = data
    TCPSocket.new(target_url, 80).close
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
