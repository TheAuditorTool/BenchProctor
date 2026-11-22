# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "redis"

class BenchmarkTest00258Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00258
    user_input = Redis.new(url: ENV.fetch("REDIS_URL", "redis://cache:6379")).get("user_data").to_s
    data = user_input.force_encoding("UTF-8")
    JSON.parse(data, create_additions: true)
    render json: { status: "ok" }
  end
end
