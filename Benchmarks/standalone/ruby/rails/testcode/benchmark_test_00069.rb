# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00069Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00069
    user_input = (params[:variables] || {})[:input].to_s
    data = format("%<value>s", value: user_input)
    unless %w[config.json index.html readme.md].include?(data.to_s)
      render json: { error: "forbidden" }, status: 403
      return
    end
    checked_path = data
    File.delete(checked_path)
    render json: { status: "ok" }
  end
end
