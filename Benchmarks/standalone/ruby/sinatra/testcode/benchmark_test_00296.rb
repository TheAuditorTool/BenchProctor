# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00296 < Sinatra::Base
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
  post "/benchmark_test_00296" do
    user_input = request.env["HTTP_ORIGIN"].to_s
    data = format("%<value>s", value: user_input)
    unless %w[config.json index.html readme.md].include?(data.to_s)
      halt 403, JSON.generate({ error: "forbidden" })
      return
    end
    checked_path = data
    File.write(checked_path, "data")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
