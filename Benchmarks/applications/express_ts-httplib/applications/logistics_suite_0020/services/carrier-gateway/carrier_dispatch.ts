// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const dispatchCarrier = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body?.field as string) || "";
  const consignment = transcript != null ? transcript : '';
  await fetch("http://manifest-builder:8080/build_manifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
