# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00123Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00123
    user_input = request.host.to_s
    data = user_input.gsub("\u0000", "")
    unless data =~ /\A[a-zA-Z0-9 _.\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    session.update(display_name: processed.to_s, updated_at: Time.now.to_i)
    render json: { status: "ok" }
  end
end
