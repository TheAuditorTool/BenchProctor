# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00148Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00148
    user_input = User.first&.name.to_s
    data = user_input.split(/[ \t]+/).join(" ")
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    session[:data] = parsed_bool.to_s
    render json: { status: "ok" }
  end
end
