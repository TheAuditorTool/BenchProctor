// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const indexDocument = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body?.multipart_field as string) || "";
  const pending: string[] = String(snippet).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const addendum: string = collected.join(',');
  await fetch("http://convert-service:8080/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
