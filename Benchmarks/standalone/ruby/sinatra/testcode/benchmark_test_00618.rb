# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00618 < Sinatra::Base
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
  post "/benchmark_test_00618" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    data = format("%<value>s", value: user_input)
    _cipher = OpenSSL::Cipher.new("aes-256-gcm")
    _cipher.encrypt
    _cipher.key = ENV.fetch("DATA_ENC_KEY", "").ljust(32)[0, 32]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
