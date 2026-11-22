// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const authorizePayment = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const remittance: string = readInput();
  await fetch("http://capture-service:8000/settle_capture", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: remittance})});
  res.json({ accepted: true });
}
