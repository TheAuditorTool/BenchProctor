# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00006Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00006
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    reader = -> { user_input.to_s.strip }
    data = reader.call
    _doc = Nokogiri::XML(data) { |config| config.nonet.nodtdload }
    _ = _doc
    render json: { status: "ok" }
  end
end
