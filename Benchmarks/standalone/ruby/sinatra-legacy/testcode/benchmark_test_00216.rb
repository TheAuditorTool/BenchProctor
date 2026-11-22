# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "securerandom"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00216 < Sinatra::Base
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
  post "/benchmark_test_00216" do
    user_input = params[:multipart_field].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    token = SecureRandom.random_bytes(16).unpack1("H*")
    DB[:reset_tokens].insert(account: data.to_s, token: token)
    content_type :json
    JSON.generate({ reset: "sent" })
  end
end
