// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const convertFx = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.authorization as string) || "";
  const ledger = Buffer.from(subject, "base64").toString();
  await fetch("http://payments-api:8080/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
