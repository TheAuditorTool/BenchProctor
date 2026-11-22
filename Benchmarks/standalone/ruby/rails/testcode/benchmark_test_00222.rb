# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00222Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00222
    user_input = ENV["APP_INPUT"] || ""
    data = user_input.gsub("\u0000", "")
    JSON.parse(data, create_additions: true)
    render json: { status: "ok" }
  end
end
