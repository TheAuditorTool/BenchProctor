# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00330 < Sinatra::Base
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
  post "/benchmark_test_00330" do
    user_input = request.env["HTTP_REFERER"].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    Object.new.instance_eval(parsed_bool.to_s)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
