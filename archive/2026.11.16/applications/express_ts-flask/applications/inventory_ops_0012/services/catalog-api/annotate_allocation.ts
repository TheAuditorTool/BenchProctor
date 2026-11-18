// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const annotateAllocation = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers["x-forwarded-for"] as string) || "";
  const _input = String(phrase);
  let backorder;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': backorder = _input.normalize('NFC'); break;
    default: backorder = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
  res.send(fileContent);
}
