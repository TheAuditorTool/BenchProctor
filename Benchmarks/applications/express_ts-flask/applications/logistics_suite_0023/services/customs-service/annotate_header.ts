// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const annotateHeader = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const parcel: string = parts.join(',');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(parcel);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const consignment = _parsed.data;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
