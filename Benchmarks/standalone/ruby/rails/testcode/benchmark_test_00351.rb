# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "securerandom"

class BenchmarkTest00351Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00351
    user_input = Comment.first&.text.to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    token = SecureRandom.hex(32)
    render json: { status: "ok" }
  end
end
