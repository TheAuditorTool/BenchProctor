# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00201 < Sinatra::Base
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
  post "/benchmark_test_00201" do
    user_input = params[:upload][:filename].to_s rescue ""
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    response.redirect(data, 303)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
