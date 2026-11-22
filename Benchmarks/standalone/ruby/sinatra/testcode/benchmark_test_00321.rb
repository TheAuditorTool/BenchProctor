# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00321 < Sinatra::Base
  before do
    halt 413 if request.content_length.to_i > 1_000_000
  end
  after do
    headers["X-Content-Type-Options"] = "nosniff"
  end

  error StandardError do
    content_type :json
    status 500
    JSON.generate({ error: "internal" })
  end
  post "/benchmark_test_00321" do
    user_input = request.body.read
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    partner = OpenSSL::X509::Certificate.new(File.read("/etc/app/partner_cert.pem"))
    envelope = OpenSSL::PKCS7.encrypt([partner], data.to_s, OpenSSL::Cipher.new("des-ede3-cbc"), OpenSSL::PKCS7::BINARY)
    content_type :json
    JSON.generate({ envelope: envelope.to_pem })
  end
end
