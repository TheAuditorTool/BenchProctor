# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00171 < Sinatra::Base
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
  post "/benchmark_test_00171" do
    user_input = request.env["HTTP_X_CUSTOM_HEADER"].to_s
    payload, _origin = user_input, 'http'
    data = payload
    _cipher = OpenSSL::Cipher.new("des-ede3-cbc")
    _cipher.encrypt
    _cipher.key = ENV.fetch("LEGACY_DES_KEY", "").ljust(24)[0, 24]
    _cipher.random_iv
    ciphertext = _cipher.update(data.to_s) + _cipher.final
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
