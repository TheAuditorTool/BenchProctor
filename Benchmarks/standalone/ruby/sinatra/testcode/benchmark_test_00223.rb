# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/http"
require "open-uri"

class BenchmarkTest00223 < Sinatra::Base
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
  post "/benchmark_test_00223" do
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    URI.open(user_input).read
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
