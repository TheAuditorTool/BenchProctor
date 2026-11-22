// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00098 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { ctx.status = 400; ctx.body = { error: "not an email address" }; return; }
  const domain = emailMatch[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00098 };
