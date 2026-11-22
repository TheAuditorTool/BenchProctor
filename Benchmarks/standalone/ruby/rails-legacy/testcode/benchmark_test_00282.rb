# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00282Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00282
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    hasher = OpenSSL::Digest.new("MD5")
    hasher.update(data.to_s)
    digest = hasher.hexdigest
    render json: { digest: digest }
  end
end
