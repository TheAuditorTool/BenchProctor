// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const publishPolicy = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(footnote);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  const fileContent = fs.readFileSync("/var/app/data/" + disbursement, "utf8");
  res.send(fileContent);
}
