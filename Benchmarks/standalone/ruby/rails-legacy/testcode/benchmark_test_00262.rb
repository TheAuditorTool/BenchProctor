# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00262Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00262
    user_input = (params[:variables] || {})[:input].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    partner = OpenSSL::X509::Certificate.new(File.read("/etc/app/partner_cert.pem"))
    envelope = OpenSSL::PKCS7.encrypt([partner], data.to_s, OpenSSL::Cipher.new("aes-256-cbc"), OpenSSL::PKCS7::BINARY)
    render json: { envelope: envelope.to_pem }
  end
end
