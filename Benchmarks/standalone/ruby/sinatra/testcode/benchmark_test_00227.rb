# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00227 < Sinatra::Base
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
  post "/benchmark_test_00227" do
    user_input = request.env["HTTP_AUTHORIZATION"].to_s
    data = sprintf("%s", user_input)
    checked_path = "/var/app/data/" + File.basename(data)
    File.delete(checked_path)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
