# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00082Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00082
    user_input = request.query_parameters[:q].to_s
    data = "#{user_input}"
    unless %w[ls cat date whoami].include?(data.to_s)
      render json: { error: "forbidden" }, status: 400
      return
    end
    IO.popen(["sh", "-c", data.to_s], &:read)
  end
end
