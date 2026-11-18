# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "digest"

class BenchmarkTest00025Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00025
    user_input = request.query_parameters[:q].to_s
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    digest = Digest::SHA256.hexdigest(data.to_s)
    render json: { status: "ok" }
  end
end
