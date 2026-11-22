# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "active_model"
require "nokogiri"

class BenchmarkTest00005Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00005
    user_input = request.referer.to_s
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    validator = Class.new do
      include ActiveModel::Validations
      attr_accessor :value
      validates :value, format: { with: /\A[a-zA-Z0-9 _.%~\-]+\z/ }
    end.new
    validator.value = data.to_s
    unless validator.valid?
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
