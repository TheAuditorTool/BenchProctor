# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00183Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00183
    user_input = request.referer.to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    cookies[:session] = { value: data, secure: true, httponly: true, same_site: :strict }
    render json: { status: "ok" }
  end
end
