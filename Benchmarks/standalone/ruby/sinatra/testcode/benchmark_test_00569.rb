# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00569 < Sinatra::Base
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
  post "/benchmark_test_00569" do
    user_input = request.cookies["session_token"].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    digest = Digest::SHA256.hexdigest(data.to_s)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
