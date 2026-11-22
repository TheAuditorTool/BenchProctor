# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00005Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00005
    user_input = request.user_agent.to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + parsed_num.to_s + "']")
    render json: { found: !account.nil? }
  end
end
