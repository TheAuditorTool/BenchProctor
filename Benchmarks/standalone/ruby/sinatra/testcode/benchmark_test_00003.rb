# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00003 < Sinatra::Base
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
  post "/benchmark_test_00003" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    content_type :html
    erb "<p><%= comment %></p>", locals: { comment: data }
  end
end
