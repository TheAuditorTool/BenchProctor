# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "open-uri"

class BenchmarkTest00163 < Sinatra::Base
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
  post "/benchmark_test_00163" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    data = user_input ? user_input : ''
    URI.open(data).read
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
