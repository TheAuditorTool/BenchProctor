// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00175(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00175 };
