// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveSummary = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers["x-forwarded-for"] as string) || "";
  const _input = String(preface);
  let cohort;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': cohort = _input.normalize('NFC'); break;
    default: cohort = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + cohort, "utf8");
  res.send(fileContent);
}
