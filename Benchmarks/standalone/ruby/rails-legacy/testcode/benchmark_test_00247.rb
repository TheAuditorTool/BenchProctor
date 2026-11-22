# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "open3"

class BenchmarkTest00247Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00247
    user_input = request.referer.to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    unless %w[ls cat date whoami].include?(data.to_s)
      render json: { error: "forbidden" }, status: 400
      return
    end
    Open3.capture2e(data.to_s)
  end
end
