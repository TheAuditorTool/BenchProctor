# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00556 < Sinatra::Base
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
  post "/benchmark_test_00556" do
    user_input = JSON.parse(request.body.read).dig("variables", "input").to_s rescue ""
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    unless data =~ /\A(asc|desc|name|created)\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    eval(processed)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
