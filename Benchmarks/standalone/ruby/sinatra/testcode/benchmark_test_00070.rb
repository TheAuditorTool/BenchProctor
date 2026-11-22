# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "cgi/escape"
require "nokogiri"

class BenchmarkTest00070 < Sinatra::Base
  before do
    halt 413 if request.content_length.to_i > 1_000_000
  end
  after do
    headers["X-Content-Type-Options"] = "nosniff"
  end

  error StandardError do
    content_type :json
    status 500
    JSON.generate({ error: "internal" })
  end
  post "/benchmark_test_00070" do
    user_input = params[:multipart_field].to_s
    data = CGI.unescape(user_input)
    handler = Class.new(Nokogiri::XML::SAX::Document) do
      attr_reader :text
      def characters(string)
        (@text ||= +"") << string
      end
    end.new
    parser = Nokogiri::XML::SAX::Parser.new(handler)
    parser.parse(data) { |ctx| ctx.replace_entities = false }
    content_type :json
    JSON.generate({ text: handler.text })
  end
end
