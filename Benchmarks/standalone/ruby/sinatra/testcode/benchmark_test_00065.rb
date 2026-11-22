# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00065 < Sinatra::Base
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
  post "/benchmark_test_00065" do
    user_input = DB[:users].first&.fetch(:name, "").to_s
    payload, _origin = user_input, 'http'
    data = payload
    unless %w[config.json index.html readme.md].include?(data.to_s)
      halt 403, JSON.generate({ error: "forbidden" })
      return
    end
    checked_path = data
    File.delete(checked_path)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
