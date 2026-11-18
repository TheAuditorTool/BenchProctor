# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/http"

class BenchmarkTest00092 < Sinatra::Base
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
  post "/benchmark_test_00092" do
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    redirect data
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
