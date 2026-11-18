// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openDispute = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers["x-forwarded-for"] as string) || "";
  const remittance = String(passage).slice(0, 200);
  await fetch("http://capture-service:8000/settle_capture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
  res.json({ accepted: true });
}
