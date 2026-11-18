# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00458 < Sinatra::Base
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
  post "/benchmark_test_00458" do
    user_input = ENV["APP_INPUT"] || ""
    _prefix = user_input[0,1].downcase
    data = case _prefix
           when 'h' then user_input.downcase
           when 'f' then user_input.upcase
           else user_input.strip
           end
    File.delete("/var/app/data/" + data)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
