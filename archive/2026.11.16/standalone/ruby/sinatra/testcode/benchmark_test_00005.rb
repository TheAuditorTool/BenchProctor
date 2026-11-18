# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/http"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00005 < Sinatra::Base
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
  post "/benchmark_test_00005" do
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    data = ''
    user_input.split(',').each { |token| data = token }
    DB.fetch("SELECT * FROM users WHERE id = '" + data + "'").all
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
