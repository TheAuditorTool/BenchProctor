# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00146Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00146
    user_input = ENV["APP_INPUT"] || ""
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    Rails.application.config.x.announcement = parsed_num.to_s
    render json: { status: "ok" }
  end
end
