// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const annotateRoster = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-forwarded-for"] as string) || "";
  const _input = String(summary);
  let bulletin;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': bulletin = _input.normalize('NFC'); break;
    default: bulletin = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + bulletin, "utf8");
  res.send(fileContent);
}
