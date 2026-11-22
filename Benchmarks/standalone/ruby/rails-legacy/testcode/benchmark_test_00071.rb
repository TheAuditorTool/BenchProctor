# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00071Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00071
    user_input = (params[:variables] || {})[:input].to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    content = File.read("/var/app/data/" + data)
    render json: { content: content }
  end
end
