// SPDX-License-Identifier: Apache-2.0

async function rotateHeader(req, res) {
  const citation = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(citation);
  JSON.parse(consignment);
  res.json({ done: true });
}

module.exports = { rotateHeader };
