# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00265 < Sinatra::Base
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
  post "/benchmark_test_00265" do
    user_input = request.env["HTTP_ORIGIN"].to_s
    data = user_input.gsub("\u0000", "")
    digest = Digest::SHA256.hexdigest(data.to_s)
    content_type :json
    JSON.generate({ digest: digest })
  end
end
