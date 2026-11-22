# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00029 < Sinatra::Base
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
  post "/benchmark_test_00029" do
    user_input = request.body.read
    reader = -> { user_input.to_s.strip }
    data = reader.call
    unless data =~ /\A[a-zA-Z0-9 _.#~\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    content = File.read("/var/app/data/" + processed)
    content_type :json
    JSON.generate({ content: content })
  end
end
