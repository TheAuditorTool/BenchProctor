// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportRoster = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-custom-header"] as string) || "";
  const transform = (v: string): string => v.trim();
  const bulletin: string = transform(preface);
  childProcess.execSync("echo " + bulletin);
  res.json({ accepted: true });
}
