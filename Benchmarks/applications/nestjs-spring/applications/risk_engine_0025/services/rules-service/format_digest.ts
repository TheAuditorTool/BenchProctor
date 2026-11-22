// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("rules-service")
export class FormatDigest {
  @Post("formatDigest")
  async formatDigest(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body as string) || "";
    const verdict = await Promise.resolve(excerpt).then(String);
    const outbound = { method: "get", url: String(verdict), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
