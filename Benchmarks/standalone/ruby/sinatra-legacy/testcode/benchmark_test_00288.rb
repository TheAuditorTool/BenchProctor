# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"
require "net/http"

class BenchmarkTest00288 < Sinatra::Base
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
  post "/benchmark_test_00288" do
    user_input = request.cookies["session_token"].to_s
    data = Base64.decode64(user_input)
    uri = URI.parse(data.to_s)
    outbound = Net::HTTP::Get.new(uri)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = uri.scheme == "https"
    reply = http.request(outbound)
    content_type :json
    JSON.generate({ upstream_status: reply.code.to_i })
  end
end
