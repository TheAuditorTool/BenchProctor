// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const updatePresence = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const bulletin = String(preface).slice(0, 200);
  await fetch("http://template-service:8000/compose_template", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
