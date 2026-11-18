// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveBatch = async (req: Request, res: Response): Promise<void> => {
  const wording = process.env.DELIVERY_INPUT_0060 || "";
  const transform = (v: string): string => v.trim();
  const remark: string = transform(wording);
  childProcess.execSync("echo " + remark);
  res.json({ accepted: true });
}
