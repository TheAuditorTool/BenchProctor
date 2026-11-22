# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00318 < Sinatra::Base
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
  post "/benchmark_test_00318" do
    user_input = request.env["HTTP_USER_AGENT"].to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    _coerced = Float(data, exception: false).to_s
    parsed_num = _coerced
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + parsed_num.to_s + "']")
    content_type :json
    JSON.generate({ found: !account.nil? })
  end
end
