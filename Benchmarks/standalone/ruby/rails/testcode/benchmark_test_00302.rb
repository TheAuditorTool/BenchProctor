# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00302Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00302
    user_input = request.headers["X-Forwarded-For"].to_s
    hasher = OpenSSL::Digest.new("MD5")
    hasher.update(user_input.to_s)
    digest = hasher.hexdigest
    render json: { digest: digest }
  end
end
