# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00573Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00573
    user_input = Comment.first&.text.to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    host = URI.parse(data).host rescue ""
    unless host =~ /\A(api\.intra\.net|cdn\.railscdn\.org)\z/
      render json: { error: "forbidden host" }, status: 403
      return
    end
    target_url = data
    redirect_to target_url, allow_other_host: true
  end
end
