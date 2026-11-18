# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00147Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00147
    user_input = request.body.read
    data = sprintf("%s", user_input)
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + data + "']")
    render json: { status: "ok" }
  end
end
