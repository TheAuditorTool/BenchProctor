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
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
    Nokogiri::XML(data) { |config| config.dtdload.noent.nonet }
    render json: { status: "ok" }
  end
end
