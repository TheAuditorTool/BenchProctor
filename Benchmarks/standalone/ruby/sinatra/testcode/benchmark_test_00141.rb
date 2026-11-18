# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"

class BenchmarkTest00141 < Sinatra::Base
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
  post "/benchmark_test_00141" do
    user_input = params[:field].to_s
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    content_type :html
    "<div>" + data + "</div>"
  end
end
