# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00129 < Sinatra::Base
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
  post "/benchmark_test_00129" do
    user_input = DB[:users].first&.fetch(:name, "").to_s
    data = "#{user_input}"
    _coerced = Integer(data, exception: false).to_s
    parsed_id = _coerced
    DB["SELECT * FROM users WHERE id = '" + parsed_id + "'"].prepare(:select, :user_lookup).call
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
