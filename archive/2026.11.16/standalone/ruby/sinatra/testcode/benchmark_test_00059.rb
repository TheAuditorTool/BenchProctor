# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00059 < Sinatra::Base
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
  post "/benchmark_test_00059" do
    user_input = request.env["HTTP_HOST"].to_s
    data = user_input.gsub("\u0000", "")
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    eval(parsed_num)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
