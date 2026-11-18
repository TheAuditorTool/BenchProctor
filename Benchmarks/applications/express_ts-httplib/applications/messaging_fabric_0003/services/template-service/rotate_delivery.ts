// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateDelivery = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.params.id as string) || "";
  const _raw = subject;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  childProcess.execSync("echo " + bulletin);
  res.json({ accepted: true });
}
