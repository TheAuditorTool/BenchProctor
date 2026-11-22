// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const registerPartner = async (req: Request, res: Response): Promise<void> => {
  const wording = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  let handshake;
  try { handshake = JSON.parse(wording).value || ""; }
  catch (e) { handshake = String(wording); }
  await fetch("http://mapping-store:8000/map_field", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
