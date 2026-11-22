# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00299Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00299
    user_input = User.first&.name.to_s
    payload, _origin = user_input, 'http'
    data = payload
    digest = Digest::SHA1.base64digest(data.to_s)
    render json: { digest: digest }
  end
end
