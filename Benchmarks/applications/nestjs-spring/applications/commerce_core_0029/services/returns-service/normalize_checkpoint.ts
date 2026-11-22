// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("returns-service")
export class NormalizeCheckpoint {
  @Post("normalizeCheckpoint")
  async normalizeCheckpoint(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers["user-agent"] as string) || "";
    const [backorder] = String(notice).split(',');
    const outbound = { method: "get", url: String(backorder), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
