// SPDX-License-Identifier: Apache-2.0

async function fetchManifest(req, res) {
  const snippet = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return snippet; } };
  const persona = payload.value;
  JSON.parse(persona);
  res.json({ done: true });
}

module.exports = { fetchManifest };
