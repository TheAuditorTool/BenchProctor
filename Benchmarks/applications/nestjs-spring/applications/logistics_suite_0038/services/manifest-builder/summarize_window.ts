// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("manifest-builder")
export class SummarizeWindow {
  @Post("summarizeWindow")
  async summarizeWindow(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const consignment = String(wording).slice(0, 200);
    const outbound = { method: "get", url: String(consignment), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
