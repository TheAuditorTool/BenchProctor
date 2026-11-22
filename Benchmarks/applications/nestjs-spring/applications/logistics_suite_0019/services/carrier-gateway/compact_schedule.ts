// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("carrier-gateway")
export class CompactSchedule {
  @Post("compactSchedule")
  async compactSchedule(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    const [parcel] = String(citation).split(',');
    const outbound = { method: "get", url: String(parcel), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
