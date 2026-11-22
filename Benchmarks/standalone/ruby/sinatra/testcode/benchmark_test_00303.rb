# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00303 < Sinatra::Base
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
  post "/benchmark_test_00303" do
    user_input = request.env["HTTP_ORIGIN"].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    redirect data
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
