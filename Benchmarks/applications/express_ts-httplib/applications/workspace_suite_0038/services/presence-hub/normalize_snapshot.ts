// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const normalizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const remark: string = transform(preface);
  childProcess.execSync("echo " + remark);
  res.json({ accepted: true });
}
