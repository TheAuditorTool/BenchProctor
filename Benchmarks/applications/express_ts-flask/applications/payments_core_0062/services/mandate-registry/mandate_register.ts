// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerMandate = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.payload as string) || "";
  const disbursement = headline != null ? headline : '';
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
  res.json({ accepted: true });
}
