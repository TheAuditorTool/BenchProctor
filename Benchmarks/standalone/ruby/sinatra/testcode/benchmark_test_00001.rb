# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "dry/schema"
require "nokogiri"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00001 < Sinatra::Base
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
  post "/benchmark_test_00001" do
    user_input = DB[:comments].first&.fetch(:text, "").to_s
    data = "#{user_input}"
    schema = Dry::Schema.Params { required(:value).filled(:string, format?: /\A[a-zA-Z0-9 _.%~\-]+\z/) }
    unless schema.call(value: data.to_s).success?
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + processed + "']")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
