# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi/escape"
require "nokogiri"

class BenchmarkTest00039Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00039
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    data = CGI.unescape(user_input)
    handler = Class.new(Nokogiri::XML::SAX::Document) do
      attr_reader :text
      def characters(string)
        (@text ||= +"") << string
      end
    end.new
    parser = Nokogiri::XML::SAX::Parser.new(handler)
    parser.parse(data) { |ctx| ctx.replace_entities = false }
    render json: { text: handler.text }
  end
end
