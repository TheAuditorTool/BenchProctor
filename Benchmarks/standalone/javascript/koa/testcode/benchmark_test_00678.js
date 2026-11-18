// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00678 = async (ctx) => {
  const userInput = ctx.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  ctx.session.data = String(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00678 };
