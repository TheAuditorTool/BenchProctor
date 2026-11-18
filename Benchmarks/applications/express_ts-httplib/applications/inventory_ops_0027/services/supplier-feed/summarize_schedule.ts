// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const summarizeSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const _raw = summary;
  const restock = (_raw && _raw.length > 0) ? _raw : 'default';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(restock);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const backorder = _parsed.data;
  childProcess.execSync("echo " + backorder);
  res.json({ accepted: true });
}
