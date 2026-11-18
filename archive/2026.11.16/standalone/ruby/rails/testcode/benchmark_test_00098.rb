# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00098Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00098
    user_input = request.query_parameters[:q].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    _cipher = OpenSSL::Cipher.new("aes-256-gcm")
    _cipher.encrypt
    _cipher.key = ENV.fetch("DATA_ENC_KEY", "").ljust(32)[0, 32]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    render json: { status: "ok" }
  end
end
