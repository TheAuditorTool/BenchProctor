// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const note = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const parts: string[] = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const addendum: string = parts.join(',');
  await fetch("http://ocr-service:8080/extract_text", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
