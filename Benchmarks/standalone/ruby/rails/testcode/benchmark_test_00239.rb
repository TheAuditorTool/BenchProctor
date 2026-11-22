# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00239Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00239
    user_input = request.headers["Authorization"].to_s
    data = sprintf("%s", user_input)
    hasher = OpenSSL::Digest.new("SHA256")
    hasher.update(data.to_s)
    digest = hasher.hexdigest
    render json: { digest: digest }
  end
end
