// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const normalizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const preface = process.env.WORKSPACE_INPUT_0038 || "";
  const transform = (v: string): string => v.trim();
  const remark: string = transform(preface);
  childProcess.execSync("echo " + remark);
  res.json({ accepted: true });
}
