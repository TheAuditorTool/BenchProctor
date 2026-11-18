# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00160 < Sinatra::Base
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
  post "/benchmark_test_00160" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    digest = Digest::MD5.hexdigest(user_input.to_s)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
