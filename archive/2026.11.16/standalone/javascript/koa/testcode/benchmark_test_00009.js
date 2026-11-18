// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00009 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00009 };
