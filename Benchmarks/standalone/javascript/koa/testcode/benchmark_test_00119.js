// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00119 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.respond = false;
  return ctx.res.writeHead(303, { Location: String(data) }).end();
}

module.exports = { BenchmarkTest00119 };
