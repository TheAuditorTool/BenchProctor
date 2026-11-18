# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "securerandom"

class BenchmarkTest00008Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00008
    user_input = request.query_parameters[:q].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    token = SecureRandom.hex(32)
    render json: { status: "ok" }
  end
end
