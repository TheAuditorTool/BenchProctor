# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi"

class BenchmarkTest00069Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00069
    user_input = request.headers["X-Forwarded-For"].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    processed = CGI.escapeHTML(data)
    render html: ("<div>" + processed + "</div>").html_safe
  end
end
