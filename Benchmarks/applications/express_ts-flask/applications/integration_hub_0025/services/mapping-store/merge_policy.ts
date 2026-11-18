// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergePolicy = async (req: Request, res: Response): Promise<void> => {
  const footnote = process.env.INTEGRATIONS_INPUT_0025 || "";
  const transform = (v: string): string => v.trim();
  const handshake: string = transform(footnote);
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
