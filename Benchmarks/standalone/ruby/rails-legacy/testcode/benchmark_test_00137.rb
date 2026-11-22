# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00137Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00137
    user_input = request.body.read
    data = format("%<value>s", value: user_input)
    aes = OpenSSL::Cipher::AES.new(256, :GCM)
    aes.encrypt
    aes.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))
    nonce = aes.random_iv
    ciphertext = nonce + aes.update(data.to_s) + aes.final + aes.auth_tag
    render json: { ciphertext: Base64.strict_encode64(ciphertext) }
  end
end
