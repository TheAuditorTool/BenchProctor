# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00619 < Sinatra::Base
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
  post "/benchmark_test_00619" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    unless data =~ /\A(asc|desc|name|created)\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + processed + "']")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
