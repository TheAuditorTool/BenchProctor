// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.authorization as string) || "";
  const _raw = snippet;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(persona);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = _parsed.data;
  childProcess.execSync("echo " + synopsis);
  res.json({ accepted: true });
}
