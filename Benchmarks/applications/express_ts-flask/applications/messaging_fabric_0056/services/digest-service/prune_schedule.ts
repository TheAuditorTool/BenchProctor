// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneSchedule = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-forwarded-for"] as string) || "";
  const bulletin = footnote != null ? footnote : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const snippet = bulletin;
  fs.writeFileSync("/var/uploads/" + snippet, "data");
  res.json({ accepted: true });
}
