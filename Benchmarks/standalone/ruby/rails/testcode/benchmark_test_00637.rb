# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"
require "nokogiri"

class BenchmarkTest00637Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00637
    user_input = request.body.read
    data = Base64.decode64(user_input)
    Nokogiri::XML(data) { |config| config.dtdload.noent.nonet }
    render json: { status: "ok" }
  end
end
