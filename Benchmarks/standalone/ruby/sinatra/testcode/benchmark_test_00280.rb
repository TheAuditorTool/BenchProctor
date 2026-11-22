# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00280 < Sinatra::Base
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
  post "/benchmark_test_00280" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    reader = -> { user_input.to_s.strip }
    data = reader.call
    hasher = OpenSSL::Digest.new("MD5")
    hasher.update(data.to_s)
    digest = hasher.hexdigest
    content_type :json
    JSON.generate({ digest: digest })
  end
end
