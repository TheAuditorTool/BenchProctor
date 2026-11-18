# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "socket"

class BenchmarkTest00293Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00293
    user_input = request.body.read
    data = ''
    user_input.split(',').each { |token| data = token }
    TCPSocket.new(data, 80).close
    render json: { status: "ok" }
  end
end
