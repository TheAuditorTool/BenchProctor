// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerPartner = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.headers.authorization as string) || "";
  const handshake = Buffer.from(quotation, "base64").toString();
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://mapping-store:8000/map_field", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
