# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"
require "digest"

class BenchmarkTest00412Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00412
    user_input = request.body.read
    data = Base64.decode64(user_input)
    digest = Digest::SHA256.hexdigest(data.to_s)
    render json: { status: "ok" }
  end
end
