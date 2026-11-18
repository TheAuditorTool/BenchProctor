// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileSnapshot = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["x-custom-header"] as string) || "";
  const _input = String(caption);
  let cohort;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': cohort = _input.normalize('NFC'); break;
    default: cohort = _input; break;
  }
  fs.writeFileSync("/var/uploads/" + cohort, "data");
  res.json({ accepted: true });
}
