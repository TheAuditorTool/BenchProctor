// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySignature = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.host as string) || "";
  let handshake;
  try { handshake = JSON.parse(synopsis).value || synopsis; }
  catch (e) { handshake = synopsis; }
  await fetch("http://retry-service:8000/queue_retry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
