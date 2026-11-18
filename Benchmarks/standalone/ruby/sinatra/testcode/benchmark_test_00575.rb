# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00575 < Sinatra::Base
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
  post "/benchmark_test_00575" do
    user_input = params[:upload][:filename].to_s rescue ""
    data = user_input.split(/[ \t]+/).join(" ")
    JSON.parse(data)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
