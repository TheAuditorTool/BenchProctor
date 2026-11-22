# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/http"

class BenchmarkTest00100 < Sinatra::Base
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
  post "/benchmark_test_00100" do
    user_input = JSON.parse(request.body.read).dig("variables", "input").to_s rescue ""
    data = JSON.parse(user_input)["value"] rescue ""
    host = URI.parse(data).host rescue ""
    unless host =~ /\A(api\.intra\.net|cdn\.railscdn\.org)\z/
      halt 403, JSON.generate({ error: "forbidden host" })
      return
    end
    target_url = data
    uri = URI.parse(target_url.to_s)
    outbound = Net::HTTP::Get.new(uri)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = uri.scheme == "https"
    reply = http.request(outbound)
    content_type :json
    JSON.generate({ upstream_status: reply.code.to_i })
  end
end
