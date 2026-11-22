// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const indexDocument = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(footnote);
  await fetch("http://convert-service:8080/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
