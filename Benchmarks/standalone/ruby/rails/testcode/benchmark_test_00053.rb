# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00053Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00053
    user_input = request.user_agent.to_s
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    _cipher = OpenSSL::Cipher.new("aes-256-gcm")
    _cipher.encrypt
    _cipher.key = ENV.fetch("DATA_ENC_KEY", "").ljust(32)[0, 32]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    render json: { status: "ok" }
  end
end
