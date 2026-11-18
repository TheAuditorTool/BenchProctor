# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "active_model"
require "nokogiri"

class BenchmarkTest00362Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00362
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
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
    Nokogiri::XML("<root/>").xpath("/root/item[@id='" + processed + "']")
    render json: { status: "ok" }
  end
end
