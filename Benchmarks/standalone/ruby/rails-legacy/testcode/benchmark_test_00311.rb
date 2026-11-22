# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "sanitize"

class BenchmarkTest00311Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00311
    user_input = request.body.read
    data = JSON.parse(user_input)["value"] rescue ""
    processed = Sanitize.fragment(data, Sanitize::Config::BASIC)
    send_data("<div>" + processed + "</div>", type: "text/html", disposition: "inline")
  end
end
