# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi"

class BenchmarkTest00002Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00002
    user_input = request.headers["X-Custom-Header"].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    processed = CGI.escapeHTML(data)
    render html: ("<div>" + processed + "</div>").html_safe
  end
end
