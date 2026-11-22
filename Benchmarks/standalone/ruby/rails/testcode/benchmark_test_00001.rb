# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "active_model"

class BenchmarkTest00001Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00001
    user_input = request.headers["Origin"].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    validator = Class.new do
      include ActiveModel::Validations
      attr_accessor :value
      validates :value, format: { with: /\A[a-zA-Z0-9 _.\-]+\z/ }
    end.new
    validator.value = data.to_s
    unless validator.valid?
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    session.update(display_name: processed.to_s, updated_at: Time.now.to_i)
    render json: { status: "ok" }
  end
end
