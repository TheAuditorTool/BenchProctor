// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichPolicy = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.params.id as string) || "";
  const phrase = decodeURIComponent(summary);
  if (!/^(asc|desc|name|created)$/.test(String(phrase))) { res.status(400).json({error:"invalid"}); return; }
  const subtitle = phrase;
  childProcess.execSync("echo " + subtitle);
  res.json({ accepted: true });
}
