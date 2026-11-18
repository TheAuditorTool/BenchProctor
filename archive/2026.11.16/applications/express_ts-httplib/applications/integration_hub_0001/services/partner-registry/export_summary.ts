// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const exportSummary = async (req: Request, res: Response): Promise<void> => {
  const quotation = process.env.INTEGRATIONS_INPUT_0001 || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(quotation);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(handshake);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const preface = _parsed.data;
  childProcess.execSync("echo " + preface);
  res.json({ accepted: true });
}
