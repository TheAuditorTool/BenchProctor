# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00231Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00231
    user_input = (params[:variables] || {})[:input].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    _cipher = OpenSSL::Cipher.new("des-ede3-cbc")
    _cipher.encrypt
    _cipher.key = ENV.fetch("LEGACY_DES_KEY", "").ljust(24)[0, 24]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    render json: { status: "ok" }
  end
end
