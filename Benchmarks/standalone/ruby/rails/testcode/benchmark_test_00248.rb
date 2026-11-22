# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00248Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00248
    user_input = params.require(:user).permit(:name)[:name].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    directory = Nokogiri::XML(File.read("/var/app/data/users.xml"))
    query = Nokogiri::XML::XPathContext.new(directory)
    roles = query.evaluate("//user[@name='" + data.to_s + "']/role")
    render json: { roles: roles.map(&:text) }
  end
end
