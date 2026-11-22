// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const storeAttachment = async (req: Request, res: Response): Promise<void> => {
  const blurb = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(blurb);
  await fetch("http://knowledge-index:8080/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ accepted: true });
}
