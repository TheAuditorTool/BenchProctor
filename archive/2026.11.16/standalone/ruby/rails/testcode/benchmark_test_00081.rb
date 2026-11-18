# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00081Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00081
    user_input = request.body.read
    _prefix = user_input[0,1].downcase
    data = case _prefix
           when 'h' then user_input.downcase
           when 'f' then user_input.upcase
           else user_input.strip
           end
    cookies[:session] = { value: data, secure: true, httponly: true, same_site: :strict }
    render json: { status: "ok" }
  end
end
