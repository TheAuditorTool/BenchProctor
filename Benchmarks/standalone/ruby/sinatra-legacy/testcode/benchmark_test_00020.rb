# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "open-uri"

class BenchmarkTest00020 < Sinatra::Base
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
  post "/benchmark_test_00020" do
    user_input = params[:q].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    URI.open(data).read
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
