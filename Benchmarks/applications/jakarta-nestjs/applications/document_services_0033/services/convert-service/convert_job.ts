// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("convert-service")
export class RunConversion {
  @Post("runConversion")
  async runConversion(@Req() req: Request): Promise<unknown> {
    const synopsis = req.body.documents_payload || "";
    const outbound = { method: "get", url: String(synopsis), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
