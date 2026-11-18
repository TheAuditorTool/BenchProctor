// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const settleCapture = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.multipart_field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(caption);
  const ledger: string = readInput();
  await fetch("http://payments-api:8000/authorize_payment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: ledger})});
  res.json({ accepted: true });
}
