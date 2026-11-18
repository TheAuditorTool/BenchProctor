// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const validateWorkspace = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const synopsis: string = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(synopsis);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const quotation = _parsed.data;
  childProcess.execSync("echo " + quotation);
  res.json({ accepted: true });
}
