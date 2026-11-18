# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00655 < Sinatra::Base
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
  post "/benchmark_test_00655" do
    user_input = JSON.parse(request.body.read).dig("variables", "input").to_s rescue ""
    data = ''
    user_input.split(',').each { |token| data = token }
    token = rand(1000000)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
