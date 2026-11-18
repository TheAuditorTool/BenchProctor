# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00185Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00185
    user_input = request.query_parameters[:q].to_s
    payload, _origin = user_input, 'http'
    data = payload
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + parsed_num + "']")
    render json: { status: "ok" }
  end
end
