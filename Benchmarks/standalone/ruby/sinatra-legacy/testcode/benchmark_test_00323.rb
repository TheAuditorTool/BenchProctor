# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "digest"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00323 < Sinatra::Base
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
  post "/benchmark_test_00323" do
    user_input = DB[:comments].first&.fetch(:text, "").to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    digest = Digest::MD5.hexdigest(data.to_s)
    content_type :json
    JSON.generate({ digest: digest })
  end
end
