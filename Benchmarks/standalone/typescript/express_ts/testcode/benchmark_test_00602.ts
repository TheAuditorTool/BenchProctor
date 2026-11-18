// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00602 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ accepted: true });
}
