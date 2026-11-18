// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishMessage = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const bulletin = String(summary).split(/[ \t]+/).join(" ");
  await fetch("http://bounce-handler:8000/record_bounce", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
