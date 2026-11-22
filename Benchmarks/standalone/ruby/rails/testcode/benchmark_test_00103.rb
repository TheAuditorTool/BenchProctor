# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00103Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00103
    user_input = request.headers["Authorization"].to_s
    unless user_input =~ /\A[a-zA-Z0-9 _.#~\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = user_input
    File.write("/var/uploads/" + processed, "data")
    render json: { status: "ok" }
  end
end
