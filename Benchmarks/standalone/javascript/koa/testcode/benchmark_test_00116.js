// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00116 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00116 };
