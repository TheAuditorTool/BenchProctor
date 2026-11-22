# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00075 < Sinatra::Base
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
  post "/benchmark_test_00075" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    unless %w[ls cat date whoami].include?(data.to_s)
      halt 400, JSON.generate({ error: "forbidden" })
      return
    end
    system(data.to_s)
  end
end
