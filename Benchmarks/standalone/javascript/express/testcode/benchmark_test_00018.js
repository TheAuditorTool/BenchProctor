// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00018(req, res) {
  const userInput = req.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  res.send("<div>" + processed + "</div>");
}

module.exports = { BenchmarkTest00018 };
