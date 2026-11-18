# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/http"
require "socket"

class BenchmarkTest00618Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00618
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    data = "%s" % user_input
    TCPSocket.new(data, 80).close
    render json: { status: "ok" }
  end
end
