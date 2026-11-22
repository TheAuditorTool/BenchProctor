// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const runSettlement = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  let remittance;
  try { remittance = JSON.parse(footnote).value || footnote; }
  catch (e) { remittance = footnote; }
  await fetch("http://dunning-service:8000/send_dunning_notice", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ accepted: true });
}
