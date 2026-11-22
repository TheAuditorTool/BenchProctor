# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00225 < Sinatra::Base
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
  post "/benchmark_test_00225" do
    user_input = request.body.read
    payload, _origin = user_input, 'http'
    data = payload
    digest = Digest::SHA256.hexdigest(data.to_s)
    content_type :json
    JSON.generate({ digest: digest })
  end
end
