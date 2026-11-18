// SPDX-License-Identifier: Apache-2.0

async function renderSnapshot(req, res) {
  const blurb = (await require("./shared").mq.receive("app-events"));
  let handshake;
  try { handshake = JSON.parse(blurb).value || ""; }
  catch (e) { handshake = String(blurb); }
  JSON.parse(handshake);
  res.json({ done: true });
}

module.exports = { renderSnapshot };
