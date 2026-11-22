# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00169 < Sinatra::Base
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
  post "/benchmark_test_00169" do
    user_input = request.env["HTTP_X_FORWARDED_FOR"].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    unless data =~ /\A[a-zA-Z0-9 _.#%\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    content_type :html
    stream do |out|
      out << "<div>" + processed + "</div>"
    end
  end
end
