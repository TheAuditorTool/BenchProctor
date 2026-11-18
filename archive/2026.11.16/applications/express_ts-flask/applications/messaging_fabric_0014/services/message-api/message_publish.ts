// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const publishMessage = async (req: Request, res: Response): Promise<void> => {
  const summary = fs.readFileSync("/tmp/data", "utf8");
  let bulletin;
  try { bulletin = JSON.parse(summary).value || ""; }
  catch (e) { bulletin = String(summary); }
  await fetch("http://presence-service:8000/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
