// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const cohort: string = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(cohort);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const gauge = _parsed.data;
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
