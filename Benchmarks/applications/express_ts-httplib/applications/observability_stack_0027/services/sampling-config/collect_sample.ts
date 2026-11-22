// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectSample = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const gauge = remark != null ? remark : '';
  childProcess.execFile("echo", [String(gauge)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
