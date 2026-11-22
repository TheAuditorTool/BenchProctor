// SPDX-License-Identifier: Apache-2.0

async function reconcileBatch(req, res) {
  const preface = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const bulletin = normalize(preface);
  JSON.parse(bulletin);
  res.json({ done: true });
}

module.exports = { reconcileBatch };
