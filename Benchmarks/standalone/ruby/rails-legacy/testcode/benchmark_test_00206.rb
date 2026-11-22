# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00206Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00206
    user_input = ENV["APP_INPUT"] || ""
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    _cipher = OpenSSL::Cipher.new("aes-256-gcm")
    _cipher.encrypt
    _cipher.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))[0, _cipher.key_len]
    iv = _cipher.random_iv
    ciphertext = iv + _cipher.update(data.to_s) + _cipher.final + _cipher.auth_tag
    render json: { ciphertext: Base64.strict_encode64(ciphertext) }
  end
end
