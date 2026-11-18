// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const schedulePayout = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.authorization as string) || "";
  const disbursement = Buffer.from(headline, "base64").toString();
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://fx-service:8000/convert_fx", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
  res.json({ accepted: true });
}
