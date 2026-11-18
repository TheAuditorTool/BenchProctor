# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00154 < Sinatra::Base
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
  post "/benchmark_test_00154" do
    user_input = params[:file][:filename].to_s rescue ""
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    resolved = File.realpath(File.join("/var/app/data", data)) rescue nil
    unless resolved && (resolved == "/var/app/data" || resolved.start_with?("/var/app/data/"))
      halt 403, JSON.generate({ error: "forbidden" })
      return
    end
    checked_path = resolved
    content = File.read(checked_path)
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
