// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const composeTemplate = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body as string) || "";
  const bulletin = String(subject).slice(0, 200);
  await fetch("http://presence-service:8000/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
