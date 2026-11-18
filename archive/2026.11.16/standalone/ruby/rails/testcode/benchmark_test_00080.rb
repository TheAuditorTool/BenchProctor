# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00080Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00080
    user_input = cookies[:session_token].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    unless %w[config.json index.html readme.md].include?(data.to_s)
      render json: { error: "forbidden" }, status: 403
      return
    end
    checked_path = data
    File.write(checked_path, "data")
    render json: { status: "ok" }
  end
end
