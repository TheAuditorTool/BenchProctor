// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("metrics-ingest")
export class PruneBatch {
  @Post("pruneBatch")
  async pruneBatch(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.authorization as string) || "";
    const gauge = String(tagline).slice(0, 200);
    const outbound = { method: "get", url: String(gauge), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
