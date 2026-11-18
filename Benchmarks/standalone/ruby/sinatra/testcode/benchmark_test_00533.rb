# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00533 < Sinatra::Base
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
  post "/benchmark_test_00533" do
    user_input = ENV["APP_INPUT"] || ""
    tokens = user_input.split(',')
    data = tokens.join(' ')
    result = DB[:users].where(name: data).first
    return halt 404, JSON.generate({ error: "not found" }) if result.nil?
    value = result[:name]
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
