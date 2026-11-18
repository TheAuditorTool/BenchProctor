// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00525(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00525 };
