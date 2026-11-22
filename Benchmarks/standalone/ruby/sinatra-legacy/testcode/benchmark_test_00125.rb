# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/http"
require "yaml"

class BenchmarkTest00125 < Sinatra::Base
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
  post "/benchmark_test_00125" do
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    data = JSON.parse(user_input)["value"] rescue ""
    YAML.safe_load(data)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
