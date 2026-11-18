# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "bunny"
require "base64"
require "yaml"

class BenchmarkTest00453Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00453
    user_input = Bunny.new(ENV.fetch("AMQP_URL", "amqp://guest:guest@broker:5672/%2F")).start.create_channel.queue("app-events", durable: true).pop[2].to_s
    data = Base64.decode64(user_input)
    YAML.unsafe_load(data)
    render json: { status: "ok" }
  end
end
