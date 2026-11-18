# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00478Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00478
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    unless data =~ /\A[a-zA-Z0-9 _.%~\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + processed + "']")
    render json: { status: "ok" }
  end
end
