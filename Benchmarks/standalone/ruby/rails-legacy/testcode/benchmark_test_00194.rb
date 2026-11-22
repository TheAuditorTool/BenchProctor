# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00194Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00194
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    _doc = Nokogiri::XML(data) { |config| config.nonet.nodtdload }
    _ = _doc
    render json: { status: "ok" }
  end
end
