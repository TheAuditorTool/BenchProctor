// SPDX-License-Identifier: Apache-2.0

async function compactManifest(req, res) {
  const tagline = (await require("./shared").mq.receive("app-events"));
  const payload = { get value() { return tagline; } };
  const rendition = payload.value;
  JSON.parse(rendition);
  res.json({ done: true });
}

module.exports = { compactManifest };
