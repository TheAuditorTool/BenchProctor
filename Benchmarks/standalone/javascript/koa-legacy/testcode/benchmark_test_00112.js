// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00112 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = Buffer.from(userInput, "hex").toString();
  ctx.respond = false;
  return ctx.res.writeHead(303, { Location: String(data) }).end();
}

module.exports = { BenchmarkTest00112 };
