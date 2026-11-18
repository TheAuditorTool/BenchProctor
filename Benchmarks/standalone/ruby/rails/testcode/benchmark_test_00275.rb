# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00275Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00275
    user_input = (params[:variables] || {})[:input].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    checked_path = "/var/app/data/" + File.basename(data)
    File.write(checked_path, "data")
    render json: { status: "ok" }
  end
end
