// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const normalizePromotion = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.query.id as string) || "";
  const [voucher] = String(subject).split(',');
  childProcess.exec("echo " + voucher, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
