# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "open-uri"

class BenchmarkTest00498 < Sinatra::Base
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
  post "/benchmark_test_00498" do
    user_input = params[:field].to_s
    _prefix = user_input[0,1].downcase
    data = case _prefix
           when 'h' then user_input.downcase
           when 'f' then user_input.upcase
           else user_input.strip
           end
    URI.open(data).read
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
