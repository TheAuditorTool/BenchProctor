# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00261Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00261
    user_input = Comment.first&.text.to_s
    data = format("%<value>s", value: user_input)
    reader = Nokogiri::XML::Reader(data) { |config| config.nonet.nodtdload }
    values = reader.map { |node| node.value if node.value? }.compact
    render json: { values: values }
  end
end
