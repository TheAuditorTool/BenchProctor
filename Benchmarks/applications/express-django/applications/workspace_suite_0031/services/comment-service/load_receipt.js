// SPDX-License-Identifier: Apache-2.0

async function loadReceipt(req, res) {
  const caption = req.headers.authorization || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const synopsis = normalize(caption);
  JSON.parse(synopsis);
  res.json({ done: true });
}

module.exports = { loadReceipt };
