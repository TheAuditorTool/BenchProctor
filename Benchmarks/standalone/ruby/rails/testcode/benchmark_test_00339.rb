# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00339Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00339
    user_input = Comment.first&.text.to_s
    data = user_input.split(/[ \t]+/).join(" ")
    send_data("<div>" + ERB::Util.html_escape(data) + "</div>", type: "text/html", disposition: "inline")
  end
end
