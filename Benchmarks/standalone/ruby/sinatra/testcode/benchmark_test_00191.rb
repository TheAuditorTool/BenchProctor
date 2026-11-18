# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "redis"
require "open-uri"

class BenchmarkTest00191 < Sinatra::Base
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
  post "/benchmark_test_00191" do
    user_input = Redis.new(url: ENV.fetch("REDIS_URL", "redis://cache:6379")).get("user_data").to_s
    data = "#{user_input}"
    URI.open(data).read
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
