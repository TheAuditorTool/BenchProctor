# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00158 < Sinatra::Base
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
  post "/benchmark_test_00158" do
    user_input = params[:field].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    response.add_header("set-cookie", Rack::Utils.set_cookie_header("session", { value: data, httponly: true, same_site: :strict }))
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
