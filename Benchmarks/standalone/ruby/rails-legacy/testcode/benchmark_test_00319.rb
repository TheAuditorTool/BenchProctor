# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00319Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00319
    user_input = params[:id].to_s
    transform = ->(v) { v.to_s.unicode_normalize(:nfc) }
    data = transform.call(user_input)
    unless data =~ /\A[a-zA-Z0-9 _.%~\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    directory = Nokogiri::XML(File.read("/var/app/data/users.xml"))
    query = Nokogiri::XML::XPathContext.new(directory)
    roles = query.evaluate("//user[@name='" + processed.to_s + "']/role")
    render json: { roles: roles.map(&:text) }
  end
end
