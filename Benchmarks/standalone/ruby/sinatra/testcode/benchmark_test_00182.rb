# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "socket"

class BenchmarkTest00182 < Sinatra::Base
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
  post "/benchmark_test_00182" do
    user_input = request.cookies["session_token"].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    TCPSocket.new(URI.parse(data.to_s).host, 80).close
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
