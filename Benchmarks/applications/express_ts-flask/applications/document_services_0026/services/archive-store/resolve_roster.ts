// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveRoster = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-forwarded-for"] as string) || "";
  const addendum = preface != null ? preface : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  fs.writeFileSync("/var/uploads/" + dossier, "data");
  res.json({ accepted: true });
}
