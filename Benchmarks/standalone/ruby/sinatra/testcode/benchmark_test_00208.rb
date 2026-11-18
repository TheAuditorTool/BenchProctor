# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00208 < Sinatra::Base
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
  post "/benchmark_test_00208" do
    user_input = request.body.read
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    JSON.parse(data)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
