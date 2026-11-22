# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00059Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00059
    user_input = request.body.read
    tokens = user_input.split(',')
    data = tokens.join(' ')
    session.update(display_name: data.to_s, updated_at: Time.now.to_i)
    render json: { status: "ok" }
  end
end
