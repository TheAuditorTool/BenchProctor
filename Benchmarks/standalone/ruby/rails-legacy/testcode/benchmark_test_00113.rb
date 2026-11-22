# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00113Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00113
    user_input = request.host.to_s
    _prefix = user_input[0,1].downcase
    data = case _prefix
           when 'h' then user_input.downcase
           when 'f' then user_input.upcase
           else user_input.strip
           end
    partner = OpenSSL::X509::Certificate.new(File.read("/etc/app/partner_cert.pem"))
    envelope = OpenSSL::PKCS7.encrypt([partner], data.to_s, OpenSSL::Cipher.new("des-ede3-cbc"), OpenSSL::PKCS7::BINARY)
    render json: { envelope: envelope.to_pem }
  end
end
