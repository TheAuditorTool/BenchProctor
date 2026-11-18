// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const acceptWebhook = async (req: Request, res: Response): Promise<void> => {
  const preface = ((req as any).file?.originalname as string) || "";
  const handshake = String(preface).slice(0, 200);
  await fetch("http://bridge-service:8000/bridge_queue", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
