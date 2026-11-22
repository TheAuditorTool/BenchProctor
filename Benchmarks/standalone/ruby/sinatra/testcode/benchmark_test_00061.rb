# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00061 < Sinatra::Base
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
  post "/benchmark_test_00061" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    data = JSON.parse(user_input)["value"] rescue ""
    content_type :html
    stream do |out|
      out << "<div>" + data + "</div>"
    end
  end
end
