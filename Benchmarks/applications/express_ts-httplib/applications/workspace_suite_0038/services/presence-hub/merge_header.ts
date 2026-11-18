// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const mergeHeader = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(preface);
  const remark: string = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(remark);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const wording = _parsed.data;
  childProcess.execSync("echo " + wording);
  res.json({ accepted: true });
}
