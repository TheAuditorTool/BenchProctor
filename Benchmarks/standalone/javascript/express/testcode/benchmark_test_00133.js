// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00133(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00133 };
