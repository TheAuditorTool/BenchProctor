# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00032Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00032
    user_input = cookies[:session_token].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    render html: ("<div>" + data + "</div>").html_safe
  end
end
