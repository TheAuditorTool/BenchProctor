// SPDX-License-Identifier: Apache-2.0

async function mergeShipment(req, res) {
  const footnote = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(footnote);
  const parcel = readInput();
  res.send("<div>" + parcel + "</div>");
}

module.exports = { mergeShipment };
