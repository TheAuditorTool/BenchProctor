// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySignature = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const payload = { get value() { return summary; } };
  const handshake = payload.value;
  await fetch("http://retry-service:8000/queue_retry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
