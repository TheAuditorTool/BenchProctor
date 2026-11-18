# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00402Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00402
    user_input = request.headers["X-Custom-Header"].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    JSON.parse(data)
    render json: { status: "ok" }
  end
end
