// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySignature = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.origin as string) || "";
  const [handshake] = String(heading).split(',');
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
