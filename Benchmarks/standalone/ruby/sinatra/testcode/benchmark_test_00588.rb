# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "bunny"
require "yaml"

class BenchmarkTest00588 < Sinatra::Base
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
  post "/benchmark_test_00588" do
    user_input = Bunny.new(ENV.fetch("AMQP_URL", "amqp://guest:guest@broker:5672/%2F")).start.create_channel.queue("app-events", durable: true).pop[2].to_s
    transform = ->(v) { v.to_s.unicode_normalize(:nfc) }
    data = transform.call(user_input)
    YAML.unsafe_load(data)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
