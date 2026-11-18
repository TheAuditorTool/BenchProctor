// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifyHeader = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.cookies?.session_token as string) || "";
  const _input = String(preface);
  let bulletin;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': bulletin = _input.normalize('NFC'); break;
    default: bulletin = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + bulletin, "utf8");
  res.send(fileContent);
}
