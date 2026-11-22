# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"
require "nokogiri"

class BenchmarkTest00015 < Sinatra::Base
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
  post "/benchmark_test_00015" do
    user_input = request.body.read
    data = Base64.decode64(user_input)
    reader = Nokogiri::XML::Reader(data) { |config| config.dtdload.noent }
    values = reader.map { |node| node.value if node.value? }.compact
    content_type :json
    JSON.generate({ values: values })
  end
end
