# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00121 < Sinatra::Base
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
  post "/benchmark_test_00121" do
    user_input = params[:q].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + data + "']")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
