# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00257 < Sinatra::Base
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
  post "/benchmark_test_00257" do
    user_input = request.env["HTTP_AUTHORIZATION"].to_s
    _coerced = %w[true 1 yes on].include?(user_input.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    RubyVM::InstructionSequence.compile(parsed_bool.to_s).eval
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
