# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00304 < Sinatra::Base
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
  post "/benchmark_test_00304" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    content_type :html
    "<div>" + data + "</div>"
  end
end
