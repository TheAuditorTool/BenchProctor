# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00194Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00194
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    handler = Class.new(Nokogiri::XML::SAX::Document) do
      attr_reader :text
      def characters(string)
        (@text ||= +"") << string
      end
    end.new
    parser = Nokogiri::XML::SAX::Parser.new(handler)
    parser.parse(user_input) { |ctx| ctx.replace_entities = true }
    render json: { text: handler.text }
  end
end
