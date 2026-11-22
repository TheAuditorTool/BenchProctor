// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00199(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  req.app.locals.announcement = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00199 };
