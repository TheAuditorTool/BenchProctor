# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00019 < Sinatra::Base
  enable :sessions
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
  post "/benchmark_test_00019" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    reader = -> { user_input.to_s.strip }
    data = reader.call
    unless data =~ /\A[a-zA-Z0-9 _.\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    session.update(display_name: processed.to_s, updated_at: Time.now.to_i)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
