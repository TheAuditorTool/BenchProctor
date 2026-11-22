# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00016 < Sinatra::Base
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
  post "/benchmark_test_00016" do
    user_input = request.env["HTTP_HOST"].to_s
    response.add_header("set-cookie", Rack::Utils.set_cookie_header("session", { value: user_input, httponly: true, same_site: :strict }))
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
