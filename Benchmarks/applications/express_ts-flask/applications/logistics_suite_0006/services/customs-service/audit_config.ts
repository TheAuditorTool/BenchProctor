// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  childProcess.execFileSync("echo", [consignment]);
  res.json({ accepted: true });
}
