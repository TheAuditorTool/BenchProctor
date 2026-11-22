// SPDX-License-Identifier: Apache-2.0

async function pruneSummary(req, res) {
  const transcript = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(transcript);
  JSON.parse(consignment);
  res.json({ done: true });
}

module.exports = { pruneSummary };
