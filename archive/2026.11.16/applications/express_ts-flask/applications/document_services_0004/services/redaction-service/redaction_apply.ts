// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const applyRedaction = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const dossier: string = normalize(excerpt);
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
