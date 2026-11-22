# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "open3"

class BenchmarkTest00233Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00233
    user_input = ENV["APP_INPUT"] || ""
    tokens = user_input.split(',')
    data = tokens.join(' ')
    Open3.capture2e("echo " + data)
    render json: { status: "ok" }
  end
end
