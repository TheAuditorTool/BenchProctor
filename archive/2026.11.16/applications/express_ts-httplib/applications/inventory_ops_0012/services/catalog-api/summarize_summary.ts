// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const summarizeSummary = async (req: Request, res: Response): Promise<void> => {
  const phrase = process.env.INVENTORY_INPUT_0012 || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(phrase);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(backorder);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const restock = _parsed.data;
  childProcess.execSync("echo " + restock);
  res.json({ accepted: true });
}
