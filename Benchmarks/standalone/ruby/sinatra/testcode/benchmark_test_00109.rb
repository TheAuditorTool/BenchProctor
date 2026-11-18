# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "cgi"
require "nokogiri"

class BenchmarkTest00109 < Sinatra::Base
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
  post "/benchmark_test_00109" do
    user_input = params[:field].to_s
    data = CGI.unescape(user_input)
    _doc = Nokogiri::XML(data) { |config| config.nonet.nodtdload }
    _ = _doc
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
