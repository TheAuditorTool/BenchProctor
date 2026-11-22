# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00058Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00058
    user_input = Comment.first&.text.to_s
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    directory = Nokogiri::XML(File.read("/var/app/data/users.xml"))
    query = Nokogiri::XML::XPathContext.new(directory)
    roles = query.evaluate("//user[@name='" + parsed_bool.to_s + "']/role")
    render json: { roles: roles.map(&:text) }
  end
end
