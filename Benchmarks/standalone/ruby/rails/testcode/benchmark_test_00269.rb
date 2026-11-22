# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/http"

class BenchmarkTest00269Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00269
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    data = "#{user_input}"
    redirect_to data, allow_other_host: true
  end
end
