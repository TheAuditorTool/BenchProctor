// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const renderCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const remark: string = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(remark);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const wording = _parsed.data;
  childProcess.execSync("echo " + wording);
  res.json({ accepted: true });
}
