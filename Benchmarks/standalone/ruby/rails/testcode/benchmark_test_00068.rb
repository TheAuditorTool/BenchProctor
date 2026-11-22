# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00068Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00068
    user_input = request.headers["Authorization"].to_s
    _coerced = %w[true 1 yes on].include?(user_input.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    RubyVM::InstructionSequence.compile(parsed_bool.to_s).eval
    render json: { status: "ok" }
  end
end
