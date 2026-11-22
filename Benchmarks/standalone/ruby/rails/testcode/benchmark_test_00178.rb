# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00178Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00178
    user_input = Comment.first&.text.to_s
    data = format("%<value>s", value: user_input)
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    session.update(display_name: parsed_num.to_s, updated_at: Time.now.to_i)
    render json: { status: "ok" }
  end
end
