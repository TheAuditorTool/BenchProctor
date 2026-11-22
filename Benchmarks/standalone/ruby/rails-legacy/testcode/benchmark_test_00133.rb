# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00133Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00133
    user_input = request.headers["Origin"].to_s
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + data.to_s + "']")
    render json: { found: !account.nil? }
  end
end
