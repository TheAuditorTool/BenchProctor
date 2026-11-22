// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00001(req, res) {
  const userInput = req.body.multipart_field || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  Object.assign(req.session, { data: String(data), expiresAt: Date.now() + 900000 });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00001 };
