// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySignature = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const handshake = summary != null ? summary : '';
  await fetch("http://retry-service:8080/queue_retry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
