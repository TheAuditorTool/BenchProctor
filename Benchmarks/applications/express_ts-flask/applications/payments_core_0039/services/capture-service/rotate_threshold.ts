// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const rotateThreshold = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.body?.payload as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(memo);
  const ledger: string = readInput();
  const fileContent = fs.readFileSync("/var/app/data/" + ledger, "utf8");
  res.send(fileContent);
}
