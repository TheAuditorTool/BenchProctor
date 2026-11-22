# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00092Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00092
    user_input = ENV["APP_INPUT"] || ""
    tokens = user_input.split(',')
    data = tokens.join(' ')
    IO.popen(["sh", "-c", "echo " + data], &:read)
    render json: { status: "ok" }
  end
end
