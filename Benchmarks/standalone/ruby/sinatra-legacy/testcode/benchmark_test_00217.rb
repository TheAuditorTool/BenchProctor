# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00217 < Sinatra::Base
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
  post "/benchmark_test_00217" do
    user_input = request.cookies["session_token"].to_s
    data = Base64.decode64(user_input)
    content_type :html
    erb "<p><%= comment %></p>", locals: { comment: data }
  end
end
