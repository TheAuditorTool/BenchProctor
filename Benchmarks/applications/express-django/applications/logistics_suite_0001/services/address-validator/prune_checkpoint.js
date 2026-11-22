// SPDX-License-Identifier: Apache-2.0

async function pruneCheckpoint(req, res) {
  const quotation = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const parcel = normalize(quotation);
  JSON.parse(parcel);
  res.json({ done: true });
}

module.exports = { pruneCheckpoint };
