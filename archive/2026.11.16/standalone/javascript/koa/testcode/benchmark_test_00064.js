// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

const BenchmarkTest00064 = async (ctx) => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00064 };
