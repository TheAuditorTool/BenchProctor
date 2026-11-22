// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateHeader = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body?.payload as string) || "";
  const backorder = notice != null ? notice : '';
  childProcess.execFile("echo", [String(backorder)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
