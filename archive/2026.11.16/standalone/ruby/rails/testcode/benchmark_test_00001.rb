# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/http"
require "socket"

class BenchmarkTest00001Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00001
    user_input = Net::HTTP.get(URI("https://api.intra.net/data"))
    payload, _origin = user_input, 'http'
    data = payload
    host = URI.parse(data).host rescue ""
    unless host =~ /\A(api\.intra\.net|cdn\.railscdn\.org)\z/
      render json: { error: "forbidden host" }, status: 403
      return
    end
    target_url = data
    TCPSocket.new(target_url, 80).close
    render json: { status: "ok" }
  end
end
