# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "dry/schema"

class BenchmarkTest00064 < Sinatra::Base
  enable :sessions
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
  post "/benchmark_test_00064" do
    user_input = ENV["APP_INPUT"] || ""
    data = "%s" % user_input
    schema = Dry::Schema.Params { required(:value).filled(:string, format?: /\A[a-zA-Z0-9 _.\-]+\z/) }
    unless schema.call(value: data.to_s).success?
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    session[:data] = processed.to_s
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
