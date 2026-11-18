// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openDispute = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const ledger: string = normalize(subtitle);
  await fetch("http://payments-api:8080/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
