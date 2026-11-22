// SPDX-License-Identifier: Apache-2.0

async function pruneBundle(req, res) {
  const phrase = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const grievance = normalize(phrase);
  JSON.parse(grievance);
  res.json({ done: true });
}

module.exports = { pruneBundle };
