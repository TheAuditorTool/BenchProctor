// SPDX-License-Identifier: Apache-2.0

async function rotateCheckpoint(req, res) {
  const citation = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(citation);
  JSON.parse(handshake);
  res.json({ done: true });
}

module.exports = { rotateCheckpoint };
