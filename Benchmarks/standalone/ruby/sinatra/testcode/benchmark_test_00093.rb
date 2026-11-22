# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00093 < Sinatra::Base
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
  post "/benchmark_test_00093" do
    user_input = request.env["HTTP_USER_AGENT"].to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    unless data =~ /\A[a-zA-Z0-9 _.\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    settings.set(:announcement, processed.to_s)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
