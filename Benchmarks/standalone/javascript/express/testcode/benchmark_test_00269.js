// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00269(req, res) {
  const userInput = req.body.multipart_field || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00269 };
