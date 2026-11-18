// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00075 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00075 };
