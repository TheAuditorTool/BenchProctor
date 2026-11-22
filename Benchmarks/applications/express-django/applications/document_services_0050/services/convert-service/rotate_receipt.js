// SPDX-License-Identifier: Apache-2.0

async function rotateReceipt(req, res) {
  const citation = req.headers.origin || "";
  const dossier = String(citation).slice(0, 200);
  JSON.parse(dossier);
  res.json({ done: true });
}

module.exports = { rotateReceipt };
