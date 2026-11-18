# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00046Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00046
    user_input = request.headers["X-Forwarded-For"].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + parsed_bool + "']")
    render json: { status: "ok" }
  end
end
