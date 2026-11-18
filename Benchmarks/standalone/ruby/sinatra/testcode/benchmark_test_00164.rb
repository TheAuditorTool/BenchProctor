# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "nokogiri"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00164 < Sinatra::Base
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
  post "/benchmark_test_00164" do
    user_input = DB[:users].first&.fetch(:name, "").to_s
    data = JSON.parse(user_input)["value"] rescue ""
    Nokogiri::XML(data) { |config| config.dtdload.noent.nonet }
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
