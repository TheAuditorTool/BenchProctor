# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00204 < Sinatra::Base
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
  post "/benchmark_test_00204" do
    user_input = ENV["APP_INPUT"] || ""
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    RubyVM::InstructionSequence.compile(parsed_num.to_s).eval
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
