// SPDX-License-Identifier: Apache-2.0

async function publishConfig(req, res) {
  const snippet = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const montage = normalize(snippet);
  JSON.parse(montage);
  res.json({ done: true });
}

module.exports = { publishConfig };
