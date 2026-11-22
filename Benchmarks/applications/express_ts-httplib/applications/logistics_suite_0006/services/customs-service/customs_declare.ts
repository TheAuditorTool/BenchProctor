// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const declareCustoms = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(summary);
  await fetch("http://address-validator:8080/validate_address", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
