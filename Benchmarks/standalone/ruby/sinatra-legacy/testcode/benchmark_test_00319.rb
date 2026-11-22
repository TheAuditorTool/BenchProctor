# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00319 < Sinatra::Base
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
  post "/benchmark_test_00319" do
    user_input = request.env["HTTP_REFERER"].to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    unless data =~ /\A[a-zA-Z0-9 _.%\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    IO.popen(["sh", "-c", "echo " + processed], &:read)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
