# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00332Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00332
    user_input = params.require(:user).permit(:name)[:name].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    handler = Class.new(Nokogiri::XML::SAX::Document) do
      attr_reader :text
      def characters(string)
        (@text ||= +"") << string
      end
    end.new
    parser = Nokogiri::XML::SAX::Parser.new(handler)
    parser.parse(data) { |ctx| ctx.replace_entities = true }
    render json: { text: handler.text }
  end
end
