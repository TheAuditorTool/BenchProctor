// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nunjucks from "nunjucks";

export const BenchmarkTest00261 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = `${userInput}`;
  const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: data });
  res.send(page);
}
