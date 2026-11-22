// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00125(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00125 };
