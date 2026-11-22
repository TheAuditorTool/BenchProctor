# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00104 < Sinatra::Base
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
  post "/benchmark_test_00104" do
    user_input = params[:q].to_s
    data = user_input.gsub("\u0000", "")
    aes = OpenSSL::Cipher::AES.new(256, :GCM)
    aes.encrypt
    aes.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))
    nonce = aes.random_iv
    ciphertext = nonce + aes.update(data.to_s) + aes.final + aes.auth_tag
    content_type :json
    JSON.generate({ ciphertext: Base64.strict_encode64(ciphertext) })
  end
end
