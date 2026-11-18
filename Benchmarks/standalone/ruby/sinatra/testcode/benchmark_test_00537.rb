# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "yaml"

class BenchmarkTest00537 < Sinatra::Base
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
  post "/benchmark_test_00537" do
    user_input = request.body.read
    YAML.unsafe_load(user_input)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
