# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00462 < Sinatra::Base
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
  post "/benchmark_test_00462" do
    user_input = request.env["HTTP_AUTHORIZATION"].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    redirect data
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
