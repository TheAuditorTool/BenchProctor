# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00603 < Sinatra::Base
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
  post "/benchmark_test_00603" do
    user_input = params[:q].to_s
    payload, _origin = user_input, 'http'
    data = payload
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + parsed_num + "']")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
