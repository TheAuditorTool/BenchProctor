// SPDX-License-Identifier: Apache-2.0

async function archiveBatch(req, res) {
  const passage = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return passage; } };
  const dossier = payload.value;
  JSON.parse(dossier);
  res.json({ done: true });
}

module.exports = { archiveBatch };
