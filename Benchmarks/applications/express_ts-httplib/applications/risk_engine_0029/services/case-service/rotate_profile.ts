// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const rotateProfile = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.cookies?.session_token as string) || "";
  const _input = String(subject);
  let grievance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': grievance = _input.normalize('NFC'); break;
    default: grievance = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + grievance, "utf8");
  res.send(fileContent);
}
