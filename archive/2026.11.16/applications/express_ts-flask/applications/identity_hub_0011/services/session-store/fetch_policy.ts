// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const fetchPolicy = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req as any).file?.originalname as string) || "";
  const persona = String(excerpt).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const wording = persona;
  fs.writeFileSync("/var/uploads/" + wording, "data");
  res.json({ accepted: true });
}
