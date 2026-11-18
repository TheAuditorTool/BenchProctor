# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00378Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00378
    user_input = User.first&.name.to_s
    _doc = Nokogiri::XML(user_input) { |config| config.nonet.nodtdload }
    _ = _doc
    render json: { status: "ok" }
  end
end
