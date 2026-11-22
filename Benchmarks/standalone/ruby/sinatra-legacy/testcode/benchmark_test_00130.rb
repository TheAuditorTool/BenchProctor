# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00130 < Sinatra::Base
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
  post "/benchmark_test_00130" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    transform = ->(v) { v.to_s.unicode_normalize(:nfc) }
    data = transform.call(user_input)
    unless %w[ls cat date whoami].include?(data.to_s)
      halt 400, JSON.generate({ error: "forbidden" })
      return
    end
    IO.popen(["sh", "-c", data.to_s], &:read)
  end
end
