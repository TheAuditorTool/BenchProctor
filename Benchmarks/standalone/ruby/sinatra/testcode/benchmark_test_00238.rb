# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00238 < Sinatra::Base
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
  post "/benchmark_test_00238" do
    user_input = params[:id].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    Object.new.instance_eval(data.to_s)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
