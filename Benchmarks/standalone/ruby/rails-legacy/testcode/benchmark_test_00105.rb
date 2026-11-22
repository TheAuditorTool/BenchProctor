# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00105Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00105
    user_input = params[:id].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    _coerced = %w[true 1 yes on].include?(data.to_s.downcase) ? "true" : "false"
    parsed_bool = _coerced
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + parsed_bool.to_s + "']")
    render json: { found: !account.nil? }
  end
end
