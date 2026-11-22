# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "sanitize"

class BenchmarkTest00328Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00328
    user_input = request.referer.to_s
    payload, _origin = user_input, 'http'
    data = payload
    processed = Sanitize.fragment(data, Sanitize::Config::BASIC)
    send_data("<div>" + processed + "</div>", type: "text/html", disposition: "inline")
  end
end
