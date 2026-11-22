// SPDX-License-Identifier: Apache-2.0

async function renderSnapshot(req, res) {
  const paragraph = req.headers.origin || "";
  const persona = String(paragraph).slice(0, 200);
  JSON.parse(persona);
  res.json({ done: true });
}

module.exports = { renderSnapshot };
