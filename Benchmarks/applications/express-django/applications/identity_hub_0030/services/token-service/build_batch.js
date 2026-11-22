// SPDX-License-Identifier: Apache-2.0

async function buildBatch(req, res) {
  const tagline = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(tagline);
  JSON.parse(persona);
  res.json({ done: true });
}

module.exports = { buildBatch };
