# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"

class BenchmarkTest00064 < Sinatra::Base
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
  post "/benchmark_test_00064" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    aes = OpenSSL::Cipher::AES.new(256, :ECB)
    aes.encrypt
    aes.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))
    ciphertext = aes.update(data.to_s) + aes.final
    content_type :json
    JSON.generate({ ciphertext: Base64.strict_encode64(ciphertext) })
  end
end
