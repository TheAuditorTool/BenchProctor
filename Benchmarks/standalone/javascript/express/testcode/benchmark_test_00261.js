// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00261(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(userInput));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00261 };
