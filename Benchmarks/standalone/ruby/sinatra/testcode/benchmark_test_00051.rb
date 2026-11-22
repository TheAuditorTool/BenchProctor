# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00051 < Sinatra::Base
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
  post "/benchmark_test_00051" do
    user_input = params[:upload][:filename].to_s rescue ""
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    hasher = OpenSSL::Digest.new("MD5")
    hasher.update(data.to_s)
    digest = hasher.hexdigest
    content_type :json
    JSON.generate({ digest: digest })
  end
end
