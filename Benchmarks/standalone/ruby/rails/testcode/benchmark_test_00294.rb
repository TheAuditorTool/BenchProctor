# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00294Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00294
    user_input = cookies[:session_token].to_s
    _coerced = Float(user_input, exception: false).to_s
    parsed_num = _coerced
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + parsed_num.to_s + "']")
    render json: { found: !account.nil? }
  end
end
