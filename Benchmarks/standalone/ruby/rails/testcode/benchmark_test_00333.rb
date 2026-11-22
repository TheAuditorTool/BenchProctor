# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00333Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00333
    user_input = ENV["APP_INPUT"] || ""
    reader = -> { user_input.to_s.strip }
    data = reader.call
    unless data =~ /\A[a-zA-Z0-9 _.%~\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + processed.to_s + "']")
    render json: { found: !account.nil? }
  end
end
