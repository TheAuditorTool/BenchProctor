# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00357 < Sinatra::Base
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
  post "/benchmark_test_00357" do
    user_input = request.env["HTTP_AUTHORIZATION"].to_s
    unless user_input =~ /\A(asc|desc|name|created)\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = user_input
    content_type :html
    "<div>" + processed + "</div>"
  end
end
