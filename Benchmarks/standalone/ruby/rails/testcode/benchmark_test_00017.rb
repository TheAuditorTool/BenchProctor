# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00017Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00017
    user_input = Profile.first&.bio.to_s
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    File.delete("/var/app/data/" + data)
    render json: { status: "ok" }
  end
end
