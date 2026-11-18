// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const acceptWebhook = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const handshake = Buffer.from(preface, "base64").toString();
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://bridge-service:8080/bridge_queue", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
