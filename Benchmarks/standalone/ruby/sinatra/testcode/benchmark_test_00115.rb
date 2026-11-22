# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"
require "shellwords"
require "open3"

class BenchmarkTest00115 < Sinatra::Base
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
  post "/benchmark_test_00115" do
    user_input = request.body.read
    data = Base64.decode64(user_input)
    processed = Shellwords.escape(data)
    Open3.capture2e("echo " + processed)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
