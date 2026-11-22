// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const compactSummary = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.origin as string) || "";
  const _input = String(subject);
  let voucher;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': voucher = _input.normalize('NFC'); break;
    default: voucher = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
  res.send(fileContent);
}
