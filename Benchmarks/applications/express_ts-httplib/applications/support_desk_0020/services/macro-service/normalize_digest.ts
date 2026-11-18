// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const normalizeDigest = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(phrase);
  childProcess.execSync("echo " + inquiry);
  res.json({ accepted: true });
}
