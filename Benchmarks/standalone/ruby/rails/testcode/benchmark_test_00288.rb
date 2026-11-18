# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00288Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00288
    user_input = cookies[:session_token].to_s
    data = Base64.decode64(user_input)
    unless data =~ /\A(asc|desc|name|created)\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    eval(processed)
    render json: { status: "ok" }
  end
end
