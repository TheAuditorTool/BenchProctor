// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  const consignment = Buffer.from(footnote, "utf-8").toString();
  await fetch("http://label-service:8000/create_label", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
