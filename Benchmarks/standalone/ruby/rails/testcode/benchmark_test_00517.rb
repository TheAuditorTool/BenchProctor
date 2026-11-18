# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00517Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00517
    user_input = Comment.first&.text.to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    cookies[:session] = { value: data, httponly: true, same_site: :strict }
    render json: { status: "ok" }
  end
end
