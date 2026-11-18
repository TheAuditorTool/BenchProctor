// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");

async function BenchmarkTest00345(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = nodeUtil.format("%s", userInput);
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  res.json({ done: true });
}

module.exports = { BenchmarkTest00345 };
