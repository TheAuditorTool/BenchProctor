# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00455Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00455
    user_input = request.user_agent.to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    render html: ("<div>" + data + "</div>").html_safe
  end
end
