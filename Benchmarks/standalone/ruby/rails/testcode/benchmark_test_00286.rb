# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00286Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00286
    user_input = request.headers["X-Forwarded-For"].to_s
    payload, _origin = user_input, 'http'
    data = payload
    render html: ("<div>" + data + "</div>").html_safe
  end
end
