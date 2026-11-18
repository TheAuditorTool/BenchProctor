// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const buildLedger = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(notice).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(persona);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const handshake = _parsed.data;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
