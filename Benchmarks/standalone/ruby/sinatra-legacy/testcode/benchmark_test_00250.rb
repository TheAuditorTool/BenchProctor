# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "open3"

class BenchmarkTest00250 < Sinatra::Base
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
  post "/benchmark_test_00250" do
    user_input = request.env["HTTP_REFERER"].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    unless %w[ls cat date whoami].include?(data.to_s)
      halt 400, JSON.generate({ error: "forbidden" })
      return
    end
    Open3.capture2e(data.to_s)
  end
end
