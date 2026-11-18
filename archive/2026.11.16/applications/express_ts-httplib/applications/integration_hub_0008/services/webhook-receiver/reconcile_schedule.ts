// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

export const reconcileSchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = process.env.INTEGRATIONS_INPUT_0008 || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(preface);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(handshake);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = _parsed.data;
  childProcess.execSync("echo " + paragraph);
  res.json({ accepted: true });
}
