# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00033Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00033
    user_input = params[:id].to_s
    _coerced = Float(user_input, exception: false).to_s
    parsed_num = _coerced
    eval(parsed_num)
    render json: { status: "ok" }
  end
end
