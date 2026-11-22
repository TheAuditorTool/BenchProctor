# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00099 < Sinatra::Base
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
  post "/benchmark_test_00099" do
    user_input = params[:upload][:filename].to_s rescue ""
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    DB[:users].with_sql("SELECT * FROM users WHERE id = '" + data + "'").all
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
