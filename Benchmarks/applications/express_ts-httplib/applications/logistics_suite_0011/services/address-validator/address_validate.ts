// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateAddress = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  await fetch("http://shipping-api:8080/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
