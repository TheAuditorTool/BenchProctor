// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00385 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00385 };
