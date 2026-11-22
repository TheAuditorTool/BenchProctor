# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00312 < Sinatra::Base
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
  post "/benchmark_test_00312" do
    user_input = request.env["HTTP_AUTHORIZATION"].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + parsed_bool + "']")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
