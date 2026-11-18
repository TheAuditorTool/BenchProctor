// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00619 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00619 };
