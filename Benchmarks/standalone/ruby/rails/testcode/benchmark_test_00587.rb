# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00587Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00587
    user_input = request.headers["Authorization"].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    digest = Digest::MD5.hexdigest(data.to_s)
    render json: { status: "ok" }
  end
end
