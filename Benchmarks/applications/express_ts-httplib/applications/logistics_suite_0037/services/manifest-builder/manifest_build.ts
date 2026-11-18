// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const buildManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = fs.readFileSync("/tmp/data", "utf8");
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(footnote);
  await fetch("http://label-service:8080/create_label", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
