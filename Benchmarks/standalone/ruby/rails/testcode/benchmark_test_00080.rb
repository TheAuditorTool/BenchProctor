# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00080Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00080
    user_input = File.read("/var/app/data.txt")
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    User.where(id: data).to_a
    render json: { status: "ok" }
  end
end
