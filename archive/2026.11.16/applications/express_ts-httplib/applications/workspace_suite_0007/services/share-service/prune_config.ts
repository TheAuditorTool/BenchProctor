// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const pruneConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = process.env.WORKSPACE_INPUT_0007 || "";
  const transform = (v: string): string => v.trim();
  const subtitle: string = transform(summary);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(subtitle);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const notice = _parsed.data;
  childProcess.execSync("echo " + notice);
  res.json({ accepted: true });
}
