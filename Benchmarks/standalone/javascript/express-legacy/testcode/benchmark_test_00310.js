// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00310(req, res) {
  const userInput = req.body.multipart_field || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  new Function("return (" + String(data) + ");")();
  res.json({ done: true });
}

module.exports = { BenchmarkTest00310 };
