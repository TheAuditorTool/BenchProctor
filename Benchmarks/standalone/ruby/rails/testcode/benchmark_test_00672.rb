# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi"
require "nokogiri"

class BenchmarkTest00672Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00672
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    data = CGI.unescape(user_input)
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + parsed_num + "']")
    render json: { status: "ok" }
  end
end
