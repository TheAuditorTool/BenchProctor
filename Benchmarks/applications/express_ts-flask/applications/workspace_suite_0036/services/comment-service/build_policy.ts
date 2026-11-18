// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const buildPolicy = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const synopsis: string = readInput();
  childProcess.execSync("echo " + synopsis);
  res.json({ accepted: true });
}
