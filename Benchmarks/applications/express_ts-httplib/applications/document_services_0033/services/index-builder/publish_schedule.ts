// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const publishSchedule = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(snippet);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  const fileContent = fs.readFileSync("/var/app/data/" + dossier, "utf8");
  res.send(fileContent);
}
