// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const summarizeLedger = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(consignment);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const parcel = _parsed.data;
  childProcess.execSync("echo " + parcel);
  res.json({ accepted: true });
}
