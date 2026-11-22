// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00170(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  eval(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00170 };
