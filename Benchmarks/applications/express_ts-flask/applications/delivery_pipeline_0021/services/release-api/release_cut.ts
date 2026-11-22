// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const cutRelease = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.payload as string) || "";
  const phrase = `${summary}`;
  await fetch("http://rollback-service:8000/trigger_rollback", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: phrase})});
  res.json({ accepted: true });
}
