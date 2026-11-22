# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00313Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00313
    user_input = User.first&.name.to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    send_data("<div>" + data + "</div>", type: "text/html", disposition: "inline")
  end
end
