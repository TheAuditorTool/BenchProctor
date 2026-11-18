# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "digest"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00227 < Sinatra::Base
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
  post "/benchmark_test_00227" do
    user_input = DB[:users].first&.fetch(:name, "").to_s
    data = [user_input].pack("H*").force_encoding("UTF-8") rescue user_input
    digest = Digest::MD5.hexdigest(data.to_s)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
