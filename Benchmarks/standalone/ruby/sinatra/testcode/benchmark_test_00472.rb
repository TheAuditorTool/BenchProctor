# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/http"

class BenchmarkTest00472 < Sinatra::Base
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
  post "/benchmark_test_00472" do
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    data = user_input ? user_input : ''
    host = URI.parse(data).host rescue ""
    unless host =~ /\A(api\.intra\.net|cdn\.railscdn\.org)\z/
      halt 403, JSON.generate({ error: "forbidden host" })
      return
    end
    target_url = data
    redirect target_url
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
