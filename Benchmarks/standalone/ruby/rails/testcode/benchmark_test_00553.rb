# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"
require "sanitize"

class BenchmarkTest00553Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00553
    user_input = User.first&.name.to_s
    data = Base64.decode64(user_input)
    processed = Sanitize.fragment(data, Sanitize::Config::BASIC)
    render html: ("<div>" + processed + "</div>").html_safe
  end
end
