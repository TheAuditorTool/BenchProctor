# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "redis"

class BenchmarkTest00307Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00307
    user_input = Redis.new(url: ENV.fetch("REDIS_URL", "redis://cache:6379")).get("user_data").to_s
    data = user_input.split(/[ \t]+/).join(" ")
    JSON.parse(data, create_additions: true)
    render json: { status: "ok" }
  end
end
