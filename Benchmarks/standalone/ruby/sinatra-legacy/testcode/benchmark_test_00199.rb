# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "sanitize"

class BenchmarkTest00199 < Sinatra::Base
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
  post "/benchmark_test_00199" do
    user_input = request.body.read
    data = JSON.parse(user_input)["value"] rescue ""
    processed = Sanitize.fragment(data, Sanitize::Config::BASIC)
    content_type :html
    stream do |out|
      out << "<div>" + processed + "</div>"
    end
  end
end
