// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const mergeIndex = async (req: Request, res: Response): Promise<void> => {
  const subtitle = process.env.PAYMENTS_INPUT_0002 || "";
  const transform = (v: string): string => v.trim();
  const ledger: string = transform(subtitle);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(ledger);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const remittance = _parsed.data;
  childProcess.execSync("echo " + remittance);
  res.json({ accepted: true });
}
