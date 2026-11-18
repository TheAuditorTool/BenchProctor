# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00086Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00086
    user_input = request.body.read
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    digest = Digest::SHA256.hexdigest(data.to_s)
    render json: { status: "ok" }
  end
end
