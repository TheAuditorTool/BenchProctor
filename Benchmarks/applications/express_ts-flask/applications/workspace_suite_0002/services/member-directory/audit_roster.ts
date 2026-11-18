// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const auditRoster = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const heading: string = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(heading);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const passage = _parsed.data;
  childProcess.execSync("echo " + passage);
  res.json({ accepted: true });
}
