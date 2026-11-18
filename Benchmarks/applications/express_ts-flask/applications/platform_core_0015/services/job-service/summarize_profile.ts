// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const summarizeProfile = async (req: Request, res: Response): Promise<void> => {
  const note = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const handshake = String(note).slice(0, 200);
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const persona = resolved;
  fs.writeFileSync(persona, "data");
  res.json({ accepted: true });
}
