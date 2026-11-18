# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "sanitize"

class BenchmarkTest00042 < Sinatra::Base
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
  post "/benchmark_test_00042" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    processed = Sanitize.fragment(data, Sanitize::Config::BASIC)
    content_type :html
    "<div>" + processed + "</div>"
  end
end
