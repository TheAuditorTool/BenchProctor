# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "rexml/document"

class BenchmarkTest00057 < Sinatra::Base
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
  post "/benchmark_test_00057" do
    user_input = params[:upload][:filename].to_s rescue ""
    data = "#{user_input}"
    unless data =~ /\A[a-zA-Z0-9 _.%~\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    directory = REXML::Document.new(File.read("/var/app/data/users.xml"))
    account = REXML::XPath.first(directory, "//user[@name='" + processed.to_s + "']")
    content_type :json
    JSON.generate({ found: !account.nil? })
  end
end
