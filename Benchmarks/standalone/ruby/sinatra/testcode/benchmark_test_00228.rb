# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "bunny"
require "open-uri"

class BenchmarkTest00228 < Sinatra::Base
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
  post "/benchmark_test_00228" do
    user_input = Bunny.new(ENV.fetch("AMQP_URL", "amqp://guest:guest@broker:5672/%2F")).start.create_channel.queue("app-events", durable: true).pop[2].to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    URI.open(data).read
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
