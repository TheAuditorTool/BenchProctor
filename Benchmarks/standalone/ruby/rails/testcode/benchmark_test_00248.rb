# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00248Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00248
    user_input = request.headers["Origin"].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    _cipher = OpenSSL::Cipher.new("des-ede3-cbc")
    _cipher.encrypt
    _cipher.key = ENV.fetch("LEGACY_DES_KEY", "").ljust(24)[0, 24]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    render json: { status: "ok" }
  end
end
