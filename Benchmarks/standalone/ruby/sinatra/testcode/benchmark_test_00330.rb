# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00330 < Sinatra::Base
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
  post "/benchmark_test_00330" do
    user_input = params[:id].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    RubyVM::InstructionSequence.compile(data.to_s).eval
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
