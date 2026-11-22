# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00031Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00031
    user_input = params.require(:upload_form).permit(:upload)[:upload].original_filename.to_s
    data = "%s" % user_input
    host = URI.parse(data).host rescue ""
    unless host =~ /\A(api\.intra\.net|cdn\.railscdn\.org)\z/
      render json: { error: "forbidden host" }, status: 403
      return
    end
    target_url = data
    response.set_header("Location", target_url)
    head :found
  end
end
