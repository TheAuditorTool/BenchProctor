# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00062 < Sinatra::Base
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
  post "/benchmark_test_00062" do
    user_input = request.env["HTTP_USER_AGENT"].to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    aes = OpenSSL::Cipher::AES.new(256, :GCM)
    aes.encrypt
    aes.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))
    nonce = aes.random_iv
    ciphertext = nonce + aes.update(data.to_s) + aes.final + aes.auth_tag
    content_type :json
    JSON.generate({ ciphertext: Base64.strict_encode64(ciphertext) })
  end
end
