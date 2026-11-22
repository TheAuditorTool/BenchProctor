# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00180Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00180
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    data = user_input.gsub("\u0000", "")
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    session.update(display_name: parsed_bool.to_s, updated_at: Time.now.to_i)
    render json: { status: "ok" }
  end
end
