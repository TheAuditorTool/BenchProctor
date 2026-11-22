# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00209 < Sinatra::Base
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
  post "/benchmark_test_00209" do
    user_input = request.env["HTTP_USER_AGENT"].to_s
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    cookie_value = Rack::Utils.escape(data.to_s)
    headers["Set-Cookie"] = "session=" + cookie_value + "; Path=/; HttpOnly; SameSite=Strict"
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
