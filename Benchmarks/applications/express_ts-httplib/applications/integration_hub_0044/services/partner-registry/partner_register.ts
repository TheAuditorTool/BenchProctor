// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const registerPartner = async (req: Request, res: Response): Promise<void> => {
  const blurb = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(blurb);
  const handshake: string = readInput();
  await fetch("http://mapping-store:8080/map_field", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
