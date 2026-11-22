# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "open-uri"

class BenchmarkTest00300Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00300
    user_input = request.query_parameters[:q].to_s
    data = format("%<value>s", value: user_input)
    URI.open(data).read
    render json: { status: "ok" }
  end
end
