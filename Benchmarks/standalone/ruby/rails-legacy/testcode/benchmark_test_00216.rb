# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00216Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00216
    user_input = User.first&.name.to_s
    data = user_input.split(/[ \t]+/).join(" ")
    aes = OpenSSL::Cipher::AES.new(256, :ECB)
    aes.encrypt
    aes.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))
    ciphertext = aes.update(data.to_s) + aes.final
    render json: { ciphertext: Base64.strict_encode64(ciphertext) }
  end
end
