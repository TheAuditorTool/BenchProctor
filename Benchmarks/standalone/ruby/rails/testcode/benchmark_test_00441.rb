# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00441Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00441
    user_input = request.headers["Origin"].to_s
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    _cipher = OpenSSL::Cipher.new("des-ede3-cbc")
    _cipher.encrypt
    _cipher.key = ENV.fetch("LEGACY_DES_KEY", "").ljust(24)[0, 24]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    render json: { status: "ok" }
  end
end
