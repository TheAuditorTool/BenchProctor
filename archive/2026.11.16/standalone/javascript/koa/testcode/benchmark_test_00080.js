// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00080 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00080 };
