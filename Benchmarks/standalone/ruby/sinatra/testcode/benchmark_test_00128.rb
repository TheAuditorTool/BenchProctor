# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "nokogiri"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00128 < Sinatra::Base
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
  post "/benchmark_test_00128" do
    user_input = DB[:comments].first&.fetch(:text, "").to_s
    data = format("%<value>s", value: user_input)
    reader = Nokogiri::XML::Reader(data) { |config| config.nonet.nodtdload }
    values = reader.map { |node| node.value if node.value? }.compact
    content_type :json
    JSON.generate({ values: values })
  end
end
