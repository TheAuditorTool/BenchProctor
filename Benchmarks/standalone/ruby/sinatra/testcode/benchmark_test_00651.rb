# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00651 < Sinatra::Base
  enable :sessions
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
  post "/benchmark_test_00651" do
    user_input = params[:id].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    session[:data] = parsed_bool.to_s
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
