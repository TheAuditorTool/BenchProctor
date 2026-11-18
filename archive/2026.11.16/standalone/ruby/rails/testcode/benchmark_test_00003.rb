# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00003Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00003
    user_input = Comment.first&.text.to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    _doc = Nokogiri::XML(data) { |config| config.nonet.nodtdload }
    _ = _doc
    render json: { status: "ok" }
  end
end
