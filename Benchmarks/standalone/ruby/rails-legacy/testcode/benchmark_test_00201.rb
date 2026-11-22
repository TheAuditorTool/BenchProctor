# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00201Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00201
    user_input = params.require(:upload_form).permit(:upload)[:upload].original_filename.to_s
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    Object.new.instance_eval(parsed_num.to_s)
    render json: { status: "ok" }
  end
end
