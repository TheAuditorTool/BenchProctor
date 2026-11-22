# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "redis"
require "socket"

class BenchmarkTest00303Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00303
    user_input = Redis.new(url: ENV.fetch("REDIS_URL", "redis://cache:6379")).get("user_data").to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    host = URI.parse(data).host rescue ""
    unless host =~ /\A(api\.intra\.net|cdn\.railscdn\.org)\z/
      render json: { error: "forbidden host" }, status: 403
      return
    end
    target_url = data
    TCPSocket.new(URI.parse(target_url.to_s).host, 80).close
    render json: { status: "ok" }
  end
end
