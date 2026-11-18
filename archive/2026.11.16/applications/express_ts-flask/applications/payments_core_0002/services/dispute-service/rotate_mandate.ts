// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const rotateMandate = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers["x-forwarded-for"] as string) || "";
  const _input = String(subtitle);
  let ledger;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': ledger = _input.normalize('NFC'); break;
    default: ledger = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + ledger, "utf8");
  res.send(fileContent);
}
