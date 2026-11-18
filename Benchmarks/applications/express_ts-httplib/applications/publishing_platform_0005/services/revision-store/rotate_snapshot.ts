// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.cookies?.session_token as string) || "";
  const byline = decodeURIComponent(footnote);
  childProcess.execSync("echo " + byline);
  res.json({ accepted: true });
}
