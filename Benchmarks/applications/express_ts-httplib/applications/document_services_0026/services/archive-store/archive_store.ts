// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body?.payload as string) || "";
  let addendum;
  try { addendum = JSON.parse(preface).value || ""; }
  catch (e) { addendum = String(preface); }
  await fetch("http://convert-service:8080/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
