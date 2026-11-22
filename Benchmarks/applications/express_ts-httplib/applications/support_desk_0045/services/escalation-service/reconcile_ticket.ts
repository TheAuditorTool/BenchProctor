// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const reconcileTicket = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.payload as string) || "";
  const inquiry = remark != null ? remark : '';
  childProcess.execFile("echo", [String(inquiry)], (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
