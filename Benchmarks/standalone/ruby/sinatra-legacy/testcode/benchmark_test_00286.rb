# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "base64"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00286 < Sinatra::Base
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
  post "/benchmark_test_00286" do
    user_input = DB[:users].first&.fetch(:name, "").to_s
    data = sprintf("%s", user_input)
    _cipher = OpenSSL::Cipher.new("des-ede3-cbc")
    _cipher.encrypt
    _cipher.key = Base64.strict_decode64(ENV.fetch("DATA_ENC_KEY"))[0, _cipher.key_len]
    iv = _cipher.random_iv
    ciphertext = iv + _cipher.update(data.to_s) + _cipher.final
    content_type :json
    JSON.generate({ ciphertext: Base64.strict_encode64(ciphertext) })
  end
end
