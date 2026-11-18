// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const fetchManifest = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(snippet);
  const persona: string = readInput();
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(persona);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = _parsed.data;
  childProcess.execSync("echo " + synopsis);
  res.json({ accepted: true });
}
