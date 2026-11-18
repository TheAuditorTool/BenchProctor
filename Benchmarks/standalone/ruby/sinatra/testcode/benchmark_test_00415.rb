# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00415 < Sinatra::Base
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
  post "/benchmark_test_00415" do
    user_input = request.env["HTTP_REFERER"].to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    response.set_cookie(:session, { value: data, secure: true, httponly: true, same_site: :strict })
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
