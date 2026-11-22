// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateAddress = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.query.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const consignment: string = readInput();
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
