// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.payload as string) || "";
  const consignment = summary != null ? summary : '';
  childProcess.execFile("echo", [String(consignment)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
