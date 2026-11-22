# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "securerandom"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00141 < Sinatra::Base
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
  post "/benchmark_test_00141" do
    user_input = params[:multipart_field].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    token = SecureRandom.alphanumeric(24)
    DB[:reset_tokens].insert(account: data.to_s, token: token)
    content_type :json
    JSON.generate({ reset: "sent" })
  end
end
