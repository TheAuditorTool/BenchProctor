// SPDX-License-Identifier: Apache-2.0

async function annotateWindow(req, res) {
  const subtitle = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(subtitle);
  JSON.parse(persona);
  res.json({ done: true });
}

module.exports = { annotateWindow };
