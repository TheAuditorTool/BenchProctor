# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/http"

class BenchmarkTest00074Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00074
    user_input = params.require(:user).permit(:name)[:name].to_s
    data = format("%<value>s", value: user_input)
    uri = URI.parse(data.to_s)
    outbound = Net::HTTP::Get.new(uri)
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = uri.scheme == "https"
    reply = http.request(outbound)
    render json: { upstream_status: reply.code.to_i }
  end
end
