# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "socket"

class BenchmarkTest00254Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00254
    user_input = request.headers["Authorization"].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    TCPSocket.new(URI.parse(data.to_s).host, 80).close
    render json: { status: "ok" }
  end
end
