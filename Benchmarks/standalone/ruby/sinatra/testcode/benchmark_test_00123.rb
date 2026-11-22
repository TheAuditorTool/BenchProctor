# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00123 < Sinatra::Base
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
  post "/benchmark_test_00123" do
    user_input = request.env["HTTP_HOST"].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    aes = OpenSSL::Cipher::AES.new(256, :ECB)
    aes.encrypt
    aes.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))
    ciphertext = aes.update(data.to_s) + aes.final
    content_type :json
    JSON.generate({ ciphertext: Base64.strict_encode64(ciphertext) })
  end
end
