// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const authorizePayment = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = footnote;
  const remittance: string = (globalThis as any).lastRequestValue;
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://capture-service:8080/settle_capture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
  res.json({ accepted: true });
}
